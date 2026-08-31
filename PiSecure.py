import os
import subprocess
import time

# Clear old frames first
frames = os.listdir("./framebuffer")
for file in frames:
    os.remove(f"./framebuffer/{file}")

# Generate new frames for 1 minute
for i in range(10*60):  # 100ms * 10 * 60
    subprocess.run(
        f"rpicam-jpeg -n -t 100ms -o ./framebuffer/{i+1}.jpeg --hflip --vflip",
        shell=True,
        executable="/bin/bash",
    )
