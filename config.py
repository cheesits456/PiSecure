# How many frames to use per video file, 1 frame = 1 second
batchSize=3600


## Adjust how many debug messages get printed
# General:
# 0 = none
# 1 = print when clearing old frames and when finished
generalDebugLevel=1
# Frame Capture:
# 0 = none
# 1 = print only when frame generator starts
# 2 = everything prior plus print after each captured frame
# 3 = everything prior plus print before attempting to capture each frame
frameCaptureDebugLevel=0
# Timestamp Generation:
# 0 = none
# 1 = print after each timestamp is added
# 2 = everything prior plus print before adding each timestamp
timestampDebugLevel=0
# Video Generation:
# 0 = none
# 1 = print after each video file finishes generating
# 2 = everything prior plus print before generating each video file
# 3 = everything prior plus print when adding each frame to the in-progress video file
videoGenerationDebugLevel=2