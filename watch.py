from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import sys
import time
import os


class GameReloader(FileSystemEventHandler):
    def __init__(self):
        self.process = None
        self.start_game()

    def start_game(self):
        # Start the game
        self.process = subprocess.Popen([sys.executable, "main.py"])

    def restart_game(self):
        # Terminate the old process and start a new one
        if self.process:
            self.process.terminate()
            self.process.wait()  # Wait until process is fully terminated
        self.start_game()

    def on_modified(self, event):
        # Restart only if a .py file is modified
        if event.src_path.endswith(".py"):
            print("Change detected in:", event.src_path)
            print("Restarting game...")
            self.restart_game()

if __name__ == "__main__":
    event_handler = GameReloader()
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
