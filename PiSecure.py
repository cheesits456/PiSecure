from picamera2 import Picamera2, Preview
import time

picam = Picamera2()

camera_config = picam.create_preview_configuration()
picam.configure(camera_config)

picam.start()

picam.capture_file("test_photo.jpg")
