import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from hashing import compute_file_hash, compare_file_hashes

# Setup logging

logging.basicConfig(
    filename=os.path.join('..', 'logs', 'integrity.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Dictionary to store { file_path: file_hash }
file_hash_map = {}

class FileMonitorHandler(FileSystemEventHandler):

   #Custom event handler that triggers on file system events

    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            logging.info(f"File created: {file_path}")

            try:
                file_hash = compute_file_hash(file_path)
                file_hash_map[file_path] = file_hash
                logging.info(f"New file hash stored: {file_hash}")
            except Exception as e:
                logging.error(f"Error computing hash for {file_path}: {e}")

    def on_modified(self, event):
        if not event.is_directory:
            file_path = event.src_path
            logging.info(f"File modified: {file_path}")

            old_hash = file_hash_map.get(file_path)
            try:
                new_hash = compute_file_hash(file_path)
                if old_hash:

                    if not compare_file_hashes(old_hash, new_hash):
                        logging.warning(f"File integrity changed for: {file_path}")

                file_hash_map[file_path] = new_hash
            except Exception as e:
                logging.error(f"Error computing hash for {file_path}: {e}")

    def on_deleted(self, event):
        if not event.is_directory:
            file_path = event.src_path
            logging.info(f"File deleted: {file_path}")

            if file_path in file_hash_map:
                del file_hash_map[file_path]

def initialize_file_hashes(folder_to_monitor):

    # Computes the intial hashes of all existing files on the computer.

    logging.info(f"Initializing file hashes in: {folder_to_monitor}")
    for root, dirs, files in os.walk(folder_to_monitor):
        for f in files:
            file_path = os.path.join(root, f)
            try:
                file_hash = compute_file_hash(file_path)
                file_hash_map[file_path] = file_hash
                logging.info(f"Initial hash for {file_path}: {file_hash}")
            except Exception as e:
                logging.error(f"Error computing hash for {file_path}: {e}")

def main(folder_to_monitor):

    #  Main function:
   # 1. Initialize file hashes
   # 2. Start watchdog observer
   # 3. Keep the script running indefinitely
   # initialize_file_hashes(folder_to_monitor)

    event_handler = FileMonitorHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_to_monitor, recursive=True)

    observer.start()
    logging.info("File Integrity Monitor started...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("File Integrity Monitor stopped by user.")
        observer.stop()

    observer.join()

if __name__ == "__main__":
    # Adjust path here to the directory you want to monitor
    folder_to_monitor = os.path.abspath("..")
    main(folder_to_monitor)
