#!/usr/bin/env python3
import os
import time
import argparse
import logging
import matplotlib as plt
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.dates import DateFormatter, date2num
import numpy as np
import pandas as pd

def save_plot(*files, colnames, title=None, filename=None, frame_rate=15):
    files = map(os.path.abspath, files)
    prev_dir = os.getcwd()
    
    df1 = pd.read_csv(interested_file)
    df2 = pd.read_csv(bored_file)
    
    dfs = []
    for file in files:
        dfs.append(pd.read_csv(file))
    
    for df in dfs:
        df = df.rename(columns=lambda x: x.strip()) 

        df['pupil_diameter'] = df['eye_lmk_x_23'] - df['eye_lmk_x_27']
        df['scale_pupil_diameter'] = df['pupil_diameter'] / df['p_scale']

    l = min(*[len(df) for df in dfs])
    
    columns=['timeframe', *colnames]
    df = pd.DataFrame(index=range(l), columns=columns)
    timeframe = pd.to_timedelta(np.arange(0, l * frame_rate, frame_rate), unit='s')

    df['timeframe'] = timeframe
    df['timeframe'] = pd.to_datetime(df['timeframe'])

    for col, _df in zip(colnames, dfs):
        df[col] = df['scale_pupil_diameter']
 
    myFmt = DateFormatter("%H:%M:%S")

    fmt, axs = plt.subplots()

    axs.set_title(title, color='0.7')
    axs.set_xlabel('timeframe (s)')
    axs.set_ylabel('pupil dilation')

    axs.xaxis.set_major_formatter(myFmt)
    for tick in axs.get_xticklabels():
        tick.set_rotation(45)

    axs.plot(df['timeframe'], df['interested'], color='#00a8b5', linewidth=2.0) #red
    axs.plot(df['timeframe'], df['bored'], color='#e62a76', linewidth=2.0) # blue

    blue_patch = mpatches.Patch(color='#00a8b5', label='Interested')
    red_patch = mpatches.Patch(color='#e62a76', label='Bored')
    axs.legend(handles=[red_patch, blue_patch], loc=4)

    if (filename):
        print('Saving plot')
        df.to_csv(filename + '.csv')
        plt.savefig(filename)
    else:
        plt.show()


def main(args):
    """ Main entry point of the merge_csv """
    # save_plot(args.interested, args.bored, args.filename)
    save_plot(, filename='hello')

if __name__ == "__main__":
    # parser = argparse.ArgumentParser()

    # parser.add_argument("-i", "--interested", help="Interested csv path", required=True)
    # parser.add_argument("-b", "--bored", help="Bored csv path", required=True)
    # parser.add_argument("-f", "--filename", help="Output filename")

    # args = parser.parse_args()
    # main(args)
