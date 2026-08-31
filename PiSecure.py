from picamera2.outputs import FfmpegOutput
from picamera2 import Picamera2
import time

picam2 = Picamera2()

video_config = picam2.create_video_configuration()
picam2.configure(video_config)

output = FfmpegOutput("test_video.mkv")

picam2.start_recording(output)
time.sleep(60)
picam2.stop_recording()