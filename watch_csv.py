import time
import shutil
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class CsvHandler(PatternMatchingEventHandler):
    """
    event.event_type
        'modified' | 'created' | 'moved' | 'deleted'
    event.is_directory
        True | False
    event.src_path
        path/to/observed/file
    """
    patterns = ["*.csv"]

    def __init__(self, app):
        PatternMatchingEventHandler.__init__(self)
        self.app = app

    def on_created(self, event): self.app.notify(event)
    def on_deleted(self, event): self.app.notify(event)
    def on_modified(self, event): self.app.notify(event)
    def on_moved(self, event): self.app.notify(event)

# class CsvObserver():

#     def __init__(self, handler, path):
#         self.observer = Observer()
#         self.observer.schedule(handler, path=path if path else '.')
#         self.observer.start()

#         try:
#             while True:
#                 time.sleep(1)
#         except KeyboardInterrupt:
#             self.observer.stop()

#         self.observer.join()


# if __name__ == '__main__':
#     import os

#     if not os.path.exists('test'):
#         os.makedirs('test')

#     test_dir = os.path.abspath('test')
#     handler = CsvHandler(lambda e: print(e.event_type, e.src_path))

#     try:
#         CsvObserver(handler, test_dir)
#     finally:
#         print('Removing test dir')
#         shutil.rmtree(test_dir)