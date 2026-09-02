#!/bin/env bash

for i in {0..10}; do
	rpicam-jpeg -n -o ./framebuffer/"$i".jpeg -q 20 -t 1ms --hflip --vflip 2>/dev/null &
	sleep 1
done