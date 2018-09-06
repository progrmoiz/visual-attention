#!/usr/bin/env bash

FOLDER_NAME="$1"
PROJECT_DIR="$HOME/Project/visual-attention"
OUTPUT_DIR="$HOME/Output/TEST/$FOLDER_NAME"

cd $OUTPUT_DIR

mkdir -p "openface_1" "openface_2" "openface_3" "data"

cd $PROJECT_DIR
./openface_img_bulk.sh "$OUTPUT_DIR/section_1" "$OUTPUT_DIR/openface_1"
./openface_img_bulk.sh "$OUTPUT_DIR/section_2" "$OUTPUT_DIR/openface_2"
./openface_img_bulk.sh "$OUTPUT_DIR/section_3" "$OUTPUT_DIR/openface_3"

python3 merge_csv.py -o "$OUTPUT_DIR/data" --output_filename "$FOLDER_NAME-1" "$OUTPUT_DIR/openface_1"
python3 merge_csv.py -o "$OUTPUT_DIR/data" --output_filename "$FOLDER_NAME-2" "$OUTPUT_DIR/openface_2"
python3 merge_csv.py -o "$OUTPUT_DIR/data" --output_filename "$FOLDER_NAME-3" "$OUTPUT_DIR/openface_3"

python3 TEST.gen_csv.1.py "$OUTPUT_DIR/data/$FOLDER_NAME-1.csv" "$OUTPUT_DIR/data/$FOLDER_NAME-2.csv" "$OUTPUT_DIR/data/$FOLDER_NAME-3.csv" -f "$OUTPUT_DIR/data/$FOLDER_NAME" 