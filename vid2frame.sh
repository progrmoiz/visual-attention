#!/usr/bin/env bash

INPUT_DIR=$(dirname $1)
OUTPUT_DIR=$HOME/output
FULL_FILENAME=$(basename $1)
FOLDERNAME="${FULL_FILENAME%%.*}-rate1"

mkdir -p $OUTPUT_DIR
mkdir -p $OUTPUT_DIR/$FOLDERNAME

ffmpeg -i $1 -r 1 -f image2 -q:v 2 -vf fps=1/15 "$OUTPUT_DIR/$FOLDERNAME/img_%03d.jpg"