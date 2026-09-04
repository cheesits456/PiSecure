import os
import subprocess
import time

from watchdog.observers import Observer

from config import debugLevel
from helpers.classes import FileCreateHandler
from helpers.functions import touch


# Clear old frames first
if debugLevel >= 1: print("Clearing old frames. . .")
for file in os.listdir("./framebuffer"):
    os.remove(f"./framebuffer/{file}")
if os.path.isfile("./stopFrameGenerator"):
    os.remove("./stopFrameGenerator")
if debugLevel >= 1: print("Done!")

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
    "╭───────────────────────────────────────────────────────────────────────────────╮",
    "│ Press 'Enter' to stop                                                         │",
    "│ If you stop with CTRL+C the frame generator will keep going in the background │",
    "│ If done by accident, remedy via running the command './stop'                  │",
    "╰───────────────────────────────────────────────────────────────────────────────╯",
    "",
    ""
]))

touch("./stopFrameGenerator")
