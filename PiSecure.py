import os
import subprocess
import time

from watchdog.observers import Observer

from helpers.classes import FileCreateHandler
from helpers.functions import touch


# Clear old frames first
print("Clearing old frames. . .")
for file in os.listdir("./framebuffer"):
    os.remove(f"./framebuffer/{file}")
print("Done!")

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
    "+-----------------------+",
    "| Press 'Enter' to stop |",
    "+-----------------------+",
    "",
    ""
]))

touch("./stopFrameGenerator")
