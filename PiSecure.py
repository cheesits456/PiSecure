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
    def on_created(self, event):
        add_timestamp_to_image(event.src_path)

def add_timestamp_to_image(path):
    time.sleep(0.05)
    print(f"Adding timestamp to {path}")

    fontFile = "./FiraCodeMono.ttf"
    fontSize = 100
    xPosition = 50
    yPosition = 2320
    
    timestamp = str(datetime.fromtimestamp(os.path.getctime(path))).split(".")[0]

    img = Image.open(path).convert("RGBA")
    font = ImageFont.truetype(fontFile, fontSize)

    # Values for black box in bottom corner
    tintColor = (0, 0, 0)
    transparency = 0.75  # 0=0%, 1=100%
    opacity = int(255 * transparency)
    # Create blank image with same dimensions as captured image
    overlay = Image.new(
        mode = "RGBA",
        size = img.size,
        color = tintColor + (0,)
    )
    # Draw black rectangle in bottom corner
    drawOverlay = ImageDraw.Draw(overlay)
    drawOverlay.rounded_rectangle(
        corners = (False, True, False, False),
        fill = tintColor + (opacity,),
        radius = 50,
        xy = [(0, 2290), (1250, 2464)],
    )
    # Overlay image with rectangle on top of captured image and convert back to RGB
    img = Image.alpha_composite(img, overlay)
    img = img.convert("RGB")
    # Print timestamp in bottom corner on top of black rectangle
    drawFinal = ImageDraw.Draw(img)
    drawFinal.text(
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

input("Press 'Enter' to stop\n")

touch("./stopFrameGenerator")


# Sleep until 10 frames generated, stop generator, wait for final frame
# time.sleep(10)
# time.sleep(1)

# # Loop over new frames and add timestamps
# for file in os.listdir("./framebuffer"):
#     add_timestamp_to_image(f"./framebuffer/{file}")
    