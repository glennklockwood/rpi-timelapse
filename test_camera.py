#!/usr/bin/env python

import picamera

cam = picamera.PiCamera()
# cam.resolution = (2592, 1944)
cam.resolution = (1920, 1080)
# cam.vflip = True
# cam.hflip = True
cam.capture('photo.jpg')
