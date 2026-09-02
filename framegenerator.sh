#!/bin/env bash

frameNumber=0

# Loop while file ./stopFrameGenerator doesn't exist
echo "Generating new frames. . ."
while [ ! -f "./stopFrameGenerator" ]; do
	# for i in {1..11}; do # Loop through numbers 0 - 10
	(( frameNumber += 1 ))
	rpicam-jpeg -n -o "./framebuffer/$frameNumber.jpeg" -q 20 -t 1ms --hflip --vflip 2>/dev/null &
	sleep 1
	# done

done
rm "./stopFrameGenerator"