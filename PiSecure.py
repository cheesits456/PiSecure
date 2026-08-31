import os
import subprocess
import time

from PIL import Image, ImageDraw, ImageFont


def add_timestamp_to_image(path):
    print(f"Adding timestamp to {path}")

    fontFile = "./FiraCodeMono.ttf"
    fontSize = 100
    xPosition = 50
    yPosition = 2320

    img = Image.open(path).convert("RGBA")
    drawMain = ImageDraw.Draw(img)
    font = ImageFont.truetype(fontFile, fontSize)

    tintColor = (0, 0, 0)
    transparency = .25  # 0=0%, 1=100%
    opacity = int(255 * transparency)
    
    overlay = Image.new(
        mode = "RGBA",
        size = img.size,
        color = tintColor + (0,)
    )
    drawOverlay = ImageDraw.Draw(overlay)
    drawOverlay.rounded_rectangle(
        corners = (False, True, False, False),
        fill = tintColor + (opacity,),
        radius = 50,
        xy = [(0, 2290), (1150, 2464)],
    )
    img = Image.alpha_composite(img, overlay)
    img = img.convert("RGB")
    
    drawMain.text(
        fill = (255, 255, 255),
        font = font,
        text = "2026-08-31 2:02PM",
        xy = (xPosition, yPosition),
    )
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
        args = f"rpicam-jpeg -n -o {savePath} -q 20 -t 1ms --hflip --vflip &",
        executable = "/bin/bash",
        shell = True,
        stderr = subprocess.DEVNULL,
        stdout = subprocess.DEVNULL,
    )
    print(f"Frame {frameNumber} generated")
    time.sleep(1)

time.sleep(1)

for file in os.listdir("./framebuffer"):
    add_timestamp_to_image(f"./framebuffer/{file}")
