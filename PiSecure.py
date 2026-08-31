from pprint import *
from picamera2 import Picamera2

picam2 = Picamera2()

# pprint(picam.sensor_modes)

picam2.start_and_record_video("test_video.mkv", duration=60)
