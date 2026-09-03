#!/bin/env bash

frameNumber=0

echo "Generating new frames. . ."

# Loop while file ./stopFrameGenerator doesn't exist
while [ ! -f "./stopFrameGenerator" ]; do
	(( frameNumber += 1 ))
	./captureframe.sh $frameNumber &
	sleep 1
done
rm "./stopFrameGenerator"
