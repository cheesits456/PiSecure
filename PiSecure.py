import os
import subprocess
import time

frames = os.listdir("./framebuffer")
print(frames)

# for i in range(10*60):  # 1 minute of footage, 100ms * 10 * 60 
#     subprocess.run(
#         f"rpicam-jpeg -n -t 100ms -o ./framebuffer/{i+1}.jpeg --hflip --vflip",
#         shell=True,
#         executable="/bin/bash",
#     )
