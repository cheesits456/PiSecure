from picamera2 import Picamera2
from libcamera import Transform

picam2 = Picamera2()

config = picam2.create_video_configuration(transform=Transform(hflip=True))
picam2.configure(config)

picam2.start_and_record_video("test_video.mkv", duration=60)  # duration in seconds
