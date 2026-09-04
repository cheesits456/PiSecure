#!/bin/env bash

frameNumber="$1"
rpicam-jpeg -n -o "./framebuffer/$frameNumber.jpeg" -q 20 -t 1ms --hflip --vflip && echo "Frame $frameNumber captured!"