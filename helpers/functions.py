import os
import time

from datetime import datetime
from PIL import Image, ImageDraw, ImageFont


def add_timestamp_to_image(path):
    time.sleep(0.02)

    # Values for timestamp in bottom corner
    fontFile = "./assets/FiraCodeMono.ttf"
    fontSize = 100
    xPosition = 50
    yPosition = 2320
    
    # Values for black box behind / around timestamp
    tintColor = (0, 0, 0)
    transparency = 0.75  # 0=0%, 1=100%
    opacity = int(255 * transparency)
    
    timestamp = str(datetime.fromtimestamp(os.path.getctime(path))).split(".")[0]

    img = Image.open(path).convert("RGBA")
    font = ImageFont.truetype(fontFile, fontSize)

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
    print(f"Timestamp added to {path}!")


def convert_frames_to_video(frameCount):
    print(f"\n\n{frameCount}\n\n")
    
    
def touch(path):
    with open(path, 'a'):
        os.utime(path, None)