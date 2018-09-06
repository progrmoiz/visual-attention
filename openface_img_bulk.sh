#!/usr/bin/env bash

# export OPENFACE_DIR=$HOME/Project/OpenFace
# OUTPUT_DIR=$HOME/output
# FULL_FILENAME=$(basename $1)
# FILENAME=${FULL_FILENAME%%.*}

# mkdir -p $OUTPUT_DIR
# mkdir -p $OUTPUT_DIR/data
# mkdir -p "$OUTPUT_DIR/$FILENAME"
# cd $OPENFACE_DIR/build

# ./bin/FaceLandmarkImg -fdir $1 -out_dir "$OUTPUT_DIR/data/$FILENAME"

# cd -

# new updated
export OPENFACE_DIR=$HOME/Project/OpenFace
INPUT_DIR=$1
OUTPUT_DIR=$2
FULL_FILENAME=$(basename $INPUT_DIR)
FILENAME=${FULL_FILENAME%%.*}

cd $OPENFACE_DIR/build
./bin/FaceLandmarkImg -fdir $INPUT_DIR -out_dir $OUTPUT_DIR
