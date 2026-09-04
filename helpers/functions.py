import cv2
import os
import time

from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

from config import batchSize, timestampDebugLevel, videoGenerationDebugLevel


def add_timestamp_to_image(path):
    time.sleep(0.02)
    if timestampDebugLevel >= 2: print(f"Adding timestamp to {path}. . .")

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
    img = img.resize((800, 600), resample=Image.NEAREST)
    img.save(path)
    if timestampDebugLevel >= 1: print(f"Timestamp added to {path}!")


def convert_frames_to_video(frameCount):
    frames = []
    for frame in range(frameCount - batchSize, frameCount):
        frames.append(f"./framebuffer/{frame + 1}.jpeg")
        
    if videoGenerationDebugLevel >= 2: print(f"Generating video file for files {frames[0]} through {frames[-1]}. . .")

    frame = cv2.imread(frames[0])
    height, width, layers = frame.shape
    timestamp = str(datetime.fromtimestamp(os.path.getctime(frames[0]))).split(".")[0]
    foldername, filename = timestamp.split(" ")
    outputFolder = f"./footage/{foldername}"
    outputFile = f"{outputFolder}/{filename}.mp4"
    
    # Make sure output folder exists
    os.makedirs(outputFolder, exist_ok=True)
    
    fourcc = cv2.VideoWriter_fourcc(*'FFV1')
    video = cv2.VideoWriter(
        filename = outputFile,
        fourcc = fourcc,
        fps = 1,
        frameSize = (width, height)
    )
    
    for imagePath in frames:
        if videoGenerationDebugLevel >= 3: print(f"Adding {imagePath} to {outputFile}. . .")
        video.write(cv2.imread(imagePath))
    
    cv2.destroyAllWindows()
    video.release()
        
    if videoGenerationDebugLevel >= 1: print(f"Generated video file for files {frames[0]} through {frames[-1]}!")


def touch(path):
    with open(path, "a"):
        os.utime(path, None)
