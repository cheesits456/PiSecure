#!/bin/env bash

frameNumber=0

echo "Generating new frames. . ."

# Loop while file ./stopFrameGenerator doesn't exist
while [ ! -f "./stopFrameGenerator" ]; do
	(( frameNumber += 1 ))
	rpicam-jpeg -n -o "./framebuffer/$frameNumber.jpeg" -q 20 -t 1ms --hflip --vflip 2>/dev/null &
	echo "Frame $frameNumber generated!"
	sleep 1
done
rm "./stopFrameGenerator"
