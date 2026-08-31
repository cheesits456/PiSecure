from picamera2 import Picamera2
from libcamera import Transform

picam2 = Picamera2()

mode = {
    "bit_depth": 8,
    "crop_limits": (680, 692, 1920, 1080),
    "exposure_limits": (75, 11766829, 20000),
    "format": SRGGB8,
    "fps": 47.57,
    "size": (1920, 1080),
    "unpacked": "SRGGB8"
}

config = picam2.create_video_configuration(transform=Transform(hflip=True, vflip=True))
picam2.configure(config)

picam2.start_and_record_video("test_video.mkv", duration=60)  # duration in seconds
