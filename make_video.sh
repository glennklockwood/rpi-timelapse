#!/usr/bin/env bash

if [ -z "$1" ]; then
    output_file="timelapse.mp4"
else
    output_file="$1"
fi
j=0
for i in capture-*.jpg
do
    ln -s $i frame$(printf "%04d" $j).jpg
    let j++
done

avconv -r 10 -i frame%04d.jpg -r 10 -vcodec libx264 "$output_file"

rm frame*.jpg
