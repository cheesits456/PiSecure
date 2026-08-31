import subprocess
import time

for i in range(10*60):  # 1 minute of footage, 100ms * 10 * 60 
    subprocess.run(
        f"rpicam-jpeg -n -t 1 -o ./framebuffer/{i+1}.jpeg --hflip --vflip",
        shell=True,
        executable="/bin/bash",
    )
    time.sleep(0.1)
