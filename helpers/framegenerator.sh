#!/bin/env bash

source "./config.py"
frameNumber=0

[[ $debugLevel -ge 1 ]] && echo "Generating new frames. . ."

# Loop while file ./stopFrameGenerator doesn't exist
while [ ! -f "./stopFrameGenerator" ]; do
	(( frameNumber += 1 ))
	[[ $debugLevel -ge 3 ]] && echo "Capturing frame ${frameNumber}. . ."
	./helpers/captureframe.sh $frameNumber &
	[[ $debugLevel -ge 2 ]] && echo "Frame ${frameNumber} captured!"
	sleep 1
done
rm "./stopFrameGenerator"
