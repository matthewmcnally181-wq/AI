from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from ai_parser import parse_command
from executor import execute
import time

class WatchHandler(FileSystemEventHandler):
    def __init__(self, command_text):
        self.command_text = command_text

    def on_created(self, event):
        if not event.is_directory:
            command = parse_command(self.command_text)
            execute(command)


def start_watcher(path, command_text):
    event_handler = WatchHandler(command_text)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    print(f"Watching {path}...")

    # run in background threadlike
    import threading
    threading.Thread(target=observer.join, daemon=True).start()