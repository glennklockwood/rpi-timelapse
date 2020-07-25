Creating Time-lapse Video with Raspberry Pi
================================================================================

Basic tools to take time-lapse videos with a Raspberry Pi and its camera module.

Usage
--------------------------------------------------------------------------------

Step 1: Mount network file system if you want to keep more frames than will fit
on the Raspberry Pi's SD card:

    # mount -t nfs -o vers=3,nolock synology.local:/volume1/glock/clovermill /mnt
    # mkdir -vp /mnt/2020-07

Step 2: Run the photo taking loop:

    ./photo_loop.py /mnt/2020-07/capture-*.jpg 2>&1 > timelapse.log

Step 3: Assemble time lapses:

    cd /mnt/2020-07 && ./make_video.sh /mnt/2020-07/timelapse.mp4

Note that this `make_video.sh` script assumes frames are `./capture-*.jpg`.
This is hard-coded.
