from watchdog.events import FileSystemEventHandler

from functions import add_timestamp_to_image


class FileChangeHandler(FileSystemEventHandler):
    def on_created(self, event):
        add_timestamp_to_image(event.src_path)