import os
import subprocess
import threading
import time

# Clear old frames first
for file in os.listdir("./framebuffer"):
    os.remove(f"./framebuffer/{file}")

# Generate new frames for 1 minute
for i in range(60):
    subprocess.run(
        f"rpicam-jpeg -n -o ./framebuffer/{i + 1}.jpeg -q 20 -t 1ms --hflip --vflip > /dev/null &",
        shell=True,
        executable="/bin/bash",
    )
    time.sleep(1)
