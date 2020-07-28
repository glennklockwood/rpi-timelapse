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

    ./photo_loop.py --resolution 1296x972 --window $((30*86400)) --timestep 3600 '/mnt/2020-07/capture-*.jpg' 2>&1 > timelapse.log

A few optional parameters are shown above:

- `--resolution 1296x972` sets the resolution of each screen grab
- `--window $((30*86400))` will cause frames more than 30 days old to be deleted automatically
- `--timestep 3600` will only capture a photo once every hour

Step 3: Assemble time lapses:

    cd /mnt/2020-07 && ./make_video.sh /mnt/2020-07/timelapse.mp4

Note that this `make_video.sh` script assumes frames are `./capture-*.jpg`.
This is hard-coded.
