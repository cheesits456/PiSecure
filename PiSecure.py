import os
import subprocess
import time

from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

# ------------------------------
#  Class / Function Definitions
# ------------------------------
class FileChangeHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        print(event.event_type, event.src_path)

    def on_created(self, event):
        print("on_created", event.src_path)
        print(event.src_path.strip())
        if((event.src_path).strip() == ".\test.xml"):        
            print("Execute your logic here!")

def add_timestamp_to_image(path):
    time.sleep(1)
    print(f"Adding timestamp to {path}")

    fontFile = "./FiraCodeMono.ttf"
    fontSize = 100
    xPosition = 50
    yPosition = 2320
    
    timestamp = str(datetime.fromtimestamp(os.path.getctime(path))).split(".")[0]

    img = Image.open(path)
    imgDraw = ImageDraw.Draw(img)
    font = ImageFont.truetype(fontFile, fontSize)
    # Color for black box in bottom corner
    tintColor = (0, 0, 0)

    # Draw black rectangle in bottom corner
    imgDraw.rounded_rectangle(
        corners = (False, True, False, False),
        fill = tintColor,
        radius = 50,
        xy = [(0, 2290), (1250, 2464)],
    )
    # Print timestamp in bottom corner on top of black rectangle
    imgDraw.text(
        fill = (255, 255, 255),
        font = font,
        text = timestamp,
        xy = (xPosition, yPosition),
    )
    img.save(path)
    
def touch(path):
    with open(path, 'a'):
        os.utime(path, None)


# Clear old frames first
print("Clearing old frames. . .")
for file in os.listdir("./framebuffer"):
    os.remove(f"./framebuffer/{file}")
print("Done!")

subprocess.run(
    args = "./framegenerator.sh &",
    executable = "/bin/bash",
    shell = True
)

event_handler = FileChangeHandler()
observer = Observer()
observer.schedule(event_handler, path='./framebuffer', recursive=False)
observer.start()

input("test")



# Sleep until 10 frames generated, stop generator, wait for final frame
# time.sleep(10)
touch("./stopFrameGenerator")
# time.sleep(1)

# # Loop over new frames and add timestamps
# for file in os.listdir("./framebuffer"):
#     add_timestamp_to_image(f"./framebuffer/{file}")
    