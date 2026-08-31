# from picamera2 import Picamera2

# picam2 = Picamera2()

# picam2.start_and_record_video("test_video.mkv", duration=60)  # duration in seconds

from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1920, 1080)
camera.capture('test_image.jpg')