import os
import subprocess
import time

from datetime import datetime
from PIL import Image, ImageDraw, ImageFont


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

time.sleep(10)

touch("./stopFrameGenerator")

# Loop over new frames and add timestamps
for file in os.listdir("./framebuffer"):
    add_timestamp_to_image(f"./framebuffer/{file}")
    