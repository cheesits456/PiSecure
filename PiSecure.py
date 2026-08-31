import os
import subprocess
import time

from PIL import Image, ImageDraw, ImageFont

def add_timestamp_to_image(path):
    print(f"Adding timestamp to {path}")

    fontFile = "./FiraCodeMono.ttf"
    fontSize = 100
    xPosition = 50
    yPosition = 2270

    img = Image.open(path)
    I1 = ImageDraw.Draw(img)
    font = ImageFont.truetype(fontFile, fontSize)

    I1.text((xPosition, yPosition), "2026-08-31 2:02PM", font=font, fill=(255, 255, 255))
    img.save(path)

# Clear old frames first
print("Clearing old frames. . .")
for file in os.listdir("./framebuffer"):
    os.remove(f"./framebuffer/{file}")
print("Done!")

# Generate new frames for 1 minute
print("Generating new frames. . .")
for i in range(3):
    frameNumber = i + 1
    savePath = f"./framebuffer/{frameNumber}.jpeg"
    subprocess.run(
        f"rpicam-jpeg -n -o {savePath} -q 20 -t 1ms --hflip --vflip &",
        executable="/bin/bash",
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    print(f"Frame {frameNumber} generated")
    time.sleep(1)
    
time.sleep(1)

for file in os.listdir("./framebuffer"):
    add_timestamp_to_image(f"./framebuffer/{file}")