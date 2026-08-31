import os
import subprocess
import threading
import time

# Clear old frames first
print("Clearing old frames . . .")
for file in os.listdir("./framebuffer"):
    os.remove(f"./framebuffer/{file}")
print("Done!")

# Generate new frames for 1 minute
for i in range(60):
    subprocess.run(
        f"rpicam-jpeg -n -o ./framebuffer/{i + 1}.jpeg -q 20 -t 1ms --hflip --vflip &",
        executable="/bin/bash",
        shell=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    time.sleep(1)
