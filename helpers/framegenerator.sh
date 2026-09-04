#!/bin/env bash

source "./config.py"
frameNumber=0

[[ $debugLevel -ge 1 ]] && echo "Generating new frames. . ."

# Loop while file ./stopFrameGenerator doesn't exist
while [ ! -f "./stopFrameGenerator" ]; do
	(( frameNumber += 1 ))
	./helpers/captureframe.sh $frameNumber &
	sleep 1
done
rm "./stopFrameGenerator"
