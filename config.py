## +-------------------------------------------------------------------------------------------------------------+
## | This file is valid as both a python script, as well as a bash script. Do not pad the '=' signs with spaces, |
## | otherwise it will no longer be a valid bash script, and the program will no longer work                     |
## +-------------------------------------------------------------------------------------------------------------+

# How many frames to use per video file, 1 frame = 1 second
batchSize=1800


# ID for the Discord server the bot is in, and your user ID (this is used to prevent others being able to run commands if they add the bot to their server)
serverID="1545545659493654548"
userID=306018440639152128


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