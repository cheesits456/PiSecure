import os
import subprocess
import time

# Clear old frames first
print("Clearing old frames. . .")
for file in os.listdir("./framebuffer"):
    os.remove(f"./framebuffer/{file}")
print("Done!")

# Generate new frames for 1 minute
print("Generating new frames. . .")
for i in range(60):
    frameNumber = i + 1
    subprocess.run(
        f"rpicam-jpeg -n -o ./framebuffer/{frameNumber}.jpeg -q 20 -t 1ms --hflip --vflip &",
        executable="/bin/bash",
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    print(f"Frame {frameNumber} generated")
    time.sleep(1)
