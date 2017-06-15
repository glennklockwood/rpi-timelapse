#!/usr/bin/env bash

j=0
for i in capture-*.jpg
do
    ln -s $i frame$(printf "%04d" $j).jpg
    let j++
done

avconv -r 10 -i frame%04d.jpg -r 10 -vcodec libx264 timelapse.mp4

rm frame*.jpg
