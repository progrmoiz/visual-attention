#!/usr/bin/env bash

# echo "$1 $2 $3"

NAME=$1
INTERESTED_VID=$2
BORED_VID=$3
OLDPWD=$(pwd)
PROJECT_DIR="$HOME/Project/visual-attention"
OUTPUT_DIR="$HOME/Output/$NAME"

mkdir -p "$OUTPUT_DIR"
cd $OUTPUT_DIR

mkdir -p "images_i" "images_b" "openface_i" "openface_b" "data"

# capture frame every 10th seconds
ffmpeg -i "$INTERESTED_VID" -f image2 -q:v 2 -vf fps=1/10 "$OUTPUT_DIR/images_i/img_%03d.jpg"
ffmpeg -i "$BORED_VID" -f image2 -q:v 2 -vf fps=1/10 "$OUTPUT_DIR/images_b/img_%03d.jpg"

cd $PROJECT_DIR
./openface_img_bulk.sh "$OUTPUT_DIR/images_i" "$OUTPUT_DIR/openface_i"
./openface_img_bulk.sh "$OUTPUT_DIR/images_b" "$OUTPUT_DIR/openface_b"

python3 merge_csv.py -o "$OUTPUT_DIR/data" --output_filename "$NAME-i" "$OUTPUT_DIR/openface_i"
python3 merge_csv.py -o "$OUTPUT_DIR/data" --output_filename "$NAME-b" "$OUTPUT_DIR/openface_b"

python3 save_plots.py -i "$OUTPUT_DIR/data/$NAME-i.csv" -b "$OUTPUT_DIR/data/$NAME-b.csv" -f "$OUTPUT_DIR/$NAME-plot"

cd $OLDPWD

mv "$INTERESTED_VID" "$OUTPUT_DIR"
mv "$BORED_VID" "$OUTPUT_DIR" 