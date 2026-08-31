from picamera2 import Picamera2

picam = Picamera2()

picam.start_and_record_video("test_video.mp4", duration = 60 * 60)
