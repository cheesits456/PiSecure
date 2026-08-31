from pprint import *
from picamera2 import Picamera2

picam = Picamera2()
config = {"format": "SRGGB8", "size": (3280, 2464)}

picam.configure(config)

# pprint(picam.sensor_modes)

picam.start_and_record_video("test_video.mp4", duration=60)
