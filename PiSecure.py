import os
import subprocess
import time

from watchdog.observers import Observer

from config import generalDebugLevel
from helpers.classes import FileCreateHandler
from helpers.functions import convert_frames_to_video, sort_frame_list_by_number, touch


# Remove 'stop' indicator file first
if os.path.isfile("./stopFrameGenerator"):
    os.remove("./stopFrameGenerator")

# Patch any old frames into new video file
if generalDebugLevel >= 1: print("Patching old frames into video file. . .")
oldFrames = os.listdir("./framebuffer")
oldFrames.sort(key=sort_frame_list_by_number)
frames = {
    "first": int(oldFrames[0].split(".")[0]),
    "last": int(oldFrames[-1].split(".")[0])
}
if len(oldFrames): convert_frames_to_video(
    frameCount = frames["last"],
    batchSize = frames["last"] - frames["first"] + 1
)

subprocess.run(
    args = "./helpers/framegenerator.sh &",
    executable = "/bin/bash",
    shell = True
)

# Observe ./framebuffer directory for newly created files
event_handler = FileCreateHandler()
observer = Observer()
observer.schedule(event_handler, path='./framebuffer/', recursive=False)
observer.start()

time.sleep(0.1)  # Small delay so that 'generating frames' message gets printed before the below message
input("\n".join([
    "",
    "╭───────────────────────────────────────────────────────────────────────────────╮",
    "│ Press 'Enter' to stop                                                         │",
    "│ If you stop with CTRL+C the frame generator will keep going in the background │",
    "│ If done by accident, remedy via running the command './stop'                  │",
    "╰───────────────────────────────────────────────────────────────────────────────╯",
    "",
    ""
]))

touch("./stopFrameGenerator")
