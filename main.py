#!/usr/bin/env python3
import os
import argparse
import pandas as pd
import tkinter as tk
from queue import Queue
from watchdog.observers import Observer
from gui import FdFrame
from watch_csv import CsvHandler

__author__ = "Moiz"
__version__ = "0.1.0"
__license__ = "MIT"

root = tk.Tk()

class App(FdFrame):

    def __init__(self, args):
        FdFrame.__init__(self, root)

        path = args.path if args.path else '/tmp'
        handler = CsvHandler(self)
        self.observer = Observer()
        self.observer.schedule(handler, path, recursive=True)

        self.queue = Queue()

        # create new label here & then add observer to call_all_watcher
        self.diameter = self.create_label('Diameter')
        self.calcdiam = self.create_label('Diameter / Scale')

        self.root.bind("<Escape>", lambda e: self.root.destroy())
        self.root.bind("<Destroy>", self.shutdown)
        self.root.bind("<<WatchdogEvent>>", self.handle_watchdog_event)

        self.observer.start()

    def notify(self, event):
        """Forward events from watchdog to GUI"""
        self.queue.put(event)
        self.root.event_generate("<<WatchdogEvent>>", when="tail")

    def handle_watchdog_event(self, event):
        """Called when watchdog posts an event"""
        watchdog_event = self.queue.get()
        self.w_diameter(watchdog_event)
        self.w_calcdiam(watchdog_event)

    def shutdown(self, event):
        """Perform safe shutdown when GUI has been destroyed"""
        self.observer.stop()
        self.observer.join()

    def mainloop(self):
        """Start the GUI loop"""
        self.root.mainloop()

    def csv_df(self, path):
        df = pd.read_csv(path)
        df = df.rename(columns=lambda x: x.strip())

        return df

    def last_df(self, path):
        df = self.csv_df(path)

        return df.tail(1)

    def w_diameter(self, event):
        last_df = self.last_df(event.src_path)
        diff = last_df['eye_lmk_x_23'] - last_df['eye_lmk_x_27']
        val = diff.iat[0]

        self.diameter.set(val)

        return val

    def w_calcdiam(self, event):
        last_df = self.last_df(event.src_path)
        diameter = self.w_diameter(event)

        p_scale = last_df['p_scale']
        val = p_scale.iat[0]

        self.calcdiam.set(val)
        
        return val

def main(args):

    # create the application
    app = App(args)

    app.master.title("Application")
    app.master.maxsize(1000, 600)

    # start the program
    app.mainloop()    # start the program

if __name__ == '__main__':
    # """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("path", help="Directory to watch")

    args = parser.parse_args()

    main(args)