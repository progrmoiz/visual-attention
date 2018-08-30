#!/usr/bin/env python3

import os
import time
import argparse
import logging
import pandas as pd

def merge_csv(input_dir, output_dir='output', output_filename='merged', t=False):
    input_dir = os.path.abspath(input_dir)
    output_dir = os.path.abspath(output_dir)
    main_dir = os.getcwd()

    os.chdir(input_dir)

    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    files.sort()

    merged = []

    for f in files:
        filename, ext = os.path.splitext(f)
        if ext == '.csv':
            print("merging: %s" % filename)
            read = pd.read_csv(f)
            read['filename'] = '%s%s' % (filename, ext)
            merged.append(read)

    result = pd.concat(merged)

    os.chdir(main_dir)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    os.chdir(output_dir)
    if t:
        result.to_csv('%s-%s.csv' % (output_filename, time.time()))
    else:
        result.to_csv('%s.csv' % (output_filename))

    # revert back to main folder
    os.chdir(main_dir)

def main(args):
    """ Main entry point of the merge_csv """
    merge_csv(args.dir, args.output, args.output_filename)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("dir", help="Directory containing csv files.")
    parser.add_argument("-o", "--output", default='output')
    parser.add_argument("--output_filename", default='merged')

    args = parser.parse_args()
    main(args)
