from pprint import *
from picamera2 import Picamera2

picam2 = Picamera2()

config = picam2.create_preview_configuration({"format": "SRGGB8", "size": (3280, 2464)})
picam2.align_configuration(config)
config["main"]

picam2.configure(config)

# pprint(picam.sensor_modes)

picam2.start_and_record_video("test_video.mp4", duration=60)
