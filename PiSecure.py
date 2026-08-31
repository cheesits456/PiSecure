from picamera2 import Picamera2
import time

picam = Picamera2()

picam.start_and_record_video("test_video.mp4", duration=5)
