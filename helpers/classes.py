from watchdog.events import FileSystemEventHandler

from helpers.functions import add_timestamp_to_image


class FileCreateHandler(FileSystemEventHandler):
    def on_created(self, event):
        add_timestamp_to_image(event.src_path)