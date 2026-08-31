from picamera2 import Picamera2
import time

picam = Picamera2()

camera_config = picam.create_preview_configuration()
picam.configure(camera_config)

picam.start()

picam.start_and_record_video("test_video.mp4", duration=5)
