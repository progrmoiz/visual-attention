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

def save_csv(file, filename=None):
    file1 = os.path.abspath(file)
    main_dir = os.getcwd()
    
    df1 = pd.read_csv(file1)
   
    df1 = df1.rename(columns=lambda x: x.strip())

    df1 = df1[df1['face'] == 0]

    df1 = df1.reset_index(drop=True)

    df1['pupil_diameter'] = df1['eye_lmk_x_23'] - df1['eye_lmk_x_27']

    df1['scale_pupil_diameter'] = df1['pupil_diameter'] / df1['p_scale']

    l = len(df1)
    
    columns=['timeframe', 'pupil_diameter']
    df = pd.DataFrame(index=range(l), columns=columns)

    rate = 5
    timeframe = pd.to_timedelta(np.arange(0, l * rate, rate), unit='s')

    df['timeframe'] = timeframe
    df['timeframe'] = pd.to_datetime(df['timeframe'])

    df['pupil_diameter'] = df1['scale_pupil_diameter']

    print(df.head())

    # myFmt = DateFormatter("%H:%M:%S")

    # fmt, axs = plt.subplots()

    # axs.set_title('Interested vs. Bored chart', color='0.7')
    # axs.set_xlabel('timeframe (s)')
    # axs.set_ylabel('pupil dilation')

    # axs.xaxis.set_major_formatter(myFmt)
    # for tick in axs.get_xticklabels():
        # tick.set_rotation(45)

    # axs.plot(df['timeframe'], df['interested'], color='#00a8b5', linewidth=2.0) #red
    # axs.plot(df['timeframe'], df['bored'], color='#e62a76', linewidth=2.0) # blue

    # blue_patch = mpatches.Patch(color='#00a8b5', label='Interested')
    # red_patch = mpatches.Patch(color='#e62a76', label='Bored')
    # axs.legend(handles=[red_patch, blue_patch], loc=4)

    df.to_csv(filename + '.csv')
    # if (filename):
        # print('Saving plot')
        # df.to_csv(filename + '.csv')
        # plt.savefig(filename)
    # else:
        # plt.show()


def main(args):
    """ Main entry point of the merge_csv """
    save_csv(*args.files, filename=args.filename)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate .csv combined section_1, 2, 3")

    parser.add_argument('files', metavar='F', type=str, nargs='+')
    parser.add_argument("-f", "--filename", help="Output filename")

    args = parser.parse_args()
    main(args)