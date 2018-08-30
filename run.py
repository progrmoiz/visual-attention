#!/usr/bin/env python3
import argparse
import subprocess

def main(args):
    """ Main entry point of the run.py """
    subprocess.call(' '.join(['./run.sh', args.filename, args.interested, args.bored]), shell=True)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--filename", help="Output filename", required=True)
    parser.add_argument("-i", "--interested", help="Interested video path", required=True)
    parser.add_argument("-b", "--bored", help="Bored video path", required=True)

    args = parser.parse_args()
    main(args)
