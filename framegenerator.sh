#!/bin/env bash

# Clear framebuffer first
rm "./framebuffer/*"

for i in {1..11}; do # Loop through numbers 0 - 10
	rpicam-jpeg -n -o ./framebuffer/"$i".jpeg -q 20 -t 1ms --hflip --vflip 2>/dev/null &
	sleep 1
done