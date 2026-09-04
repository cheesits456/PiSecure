from concurrent.futures import ThreadPoolExecutor
from watchdog.events import FileSystemEventHandler

from helpers.functions import add_timestamp_to_image


class FileCreateHandler(FileSystemEventHandler):
    def on_created(self, event):
        with ThreadPoolExecutor(max_workers=4) as executor:

            add_timestamp_to_image(event.src_path)

            # The variable event.src_path == './framebuffer/n.jpeg', where 'n' is the frame number
            frameNumber = int(event.src_path.split("/")[2].split(".")[0])
            if not frameNumber % 10:
                executor.submit(print, "10 images captured!")
                