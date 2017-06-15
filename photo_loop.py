#!/usr/bin/env python

import os
import time
import glob
import datetime
import picamera
import argparse

DEFAULT_TIMESTEP = datetime.timedelta(seconds=5)
DEFAULT_WINDOW = datetime.timedelta(minutes=1)
DEFAULT_OUTPUT = "/home/glock/cam/capture-%s.jpg"

def get_oldest_file(file_list):
    oldest_file = (None, datetime.datetime.now())
    for file_name in file_list:
        ctime = os.path.getctime(file_name)
        if ctime < oldest_file:
            print "replacing", oldest_file
            oldest_file = (file_name, ctime)
            print "with", oldest_file
    return oldest_file


def get_files_before(before, file_list):
    files_before = []
    for file_name in file_list:
        ctime = os.path.getctime(file_name)
        if datetime.datetime.fromtimestamp(ctime) < before:
            files_before.append(file_name)
    return files_before

def log_msg(msg):
    print datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]"), msg

def camera_loop(timestep, window_width, output_template, dry_run=False):
    cam = picamera.PiCamera()
    while True:
        loop_start = datetime.datetime.now()
        output_file = output_template % loop_start.strftime("%Y%m%d%H%M%S")
        file_list = glob.glob(output_template % "*")
        expire_files = get_files_before((loop_start - window_width),
                                        file_list)
        if not dry_run:
            cam.capture(output_file)
        log_msg("Capturing to %s" % output_file)
        for file_name in expire_files:
            if not dry_run:
                os.unlink(file_name)
            log_msg("Removing %s because it is older than %d sec" % (
                file_name,
                window_width.total_seconds()))
        time.sleep( (timestep - (datetime.datetime.now() - loop_start)).total_seconds() )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--timestep', default=None, type=int, help="time between successive photos in seconds (default=300)")
    parser.add_argument('-w', '--window', default=None, type=int, help="window of time over which photos should be retained (default=86400)")
    parser.add_argument('-o', '--output', default=None, type=str, help="full path to output files; must contain '*' where date is substituted")
    parser.add_argument('-d', '--dryrun', default=False, action='store_true', help="don't actually take photos or delete old files")
    args = parser.parse_args()

    if args.timestep is None:
        timestep = DEFAULT_TIMESTEP
    else:
        timestep = datetime.timedelta(seconds=args.timestep)
    if args.window is None:
        window_width = DEFAULT_WINDOW 
    else:
        window_width = datetime.timedelta(seconds=args.window)
    if args.output is None:
        output_template = DEFAULT_OUTPUT
    else:
        output_template = args.output.replace("*", "%s")
        
    camera_loop(timestep=timestep,
                window_width=window_width,
                output_template=output_template,
                dry_run=args.dryrun)