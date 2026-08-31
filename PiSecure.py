import subprocess
import time

for i in range(60):
    subprocess.run(
        f"rpicam-jpeg -n -t 1 -o {i+1}.jpeg --hflip --vflip",
        shell=True,
        executable="/bin/bash",
    )
    time.sleep(1)
