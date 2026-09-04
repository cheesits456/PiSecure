#!/bin/env bash

source "./config.py"
frameNumber=0

if [[ $debugLevel -ge 1 ]]; then echo "Generating new frames. . ."; echo; fi

# Loop while file ./stopFrameGenerator doesn't exist
while [ ! -f "./stopFrameGenerator" ]; do
	(( frameNumber += 1 ))
	./helpers/captureframe.sh $frameNumber &
	sleep 1
done
rm "./stopFrameGenerator"
