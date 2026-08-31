from picamera2.encoders import H264Encoder, Quality
from picamera2 import Picamera2
import time

picam2 = Picamera2()

video_config = picam2.create_video_configuration()
picam2.configure(video_config)

encoder = H264Encoder()
output = "test_video.mkv"
quality = Quality.HIGH

picam2.start_recording(encoder, output, quality)
time.sleep(60)
picam2.stop_recording()