#!/bin/bash
cd "$(dirname "$0")"  # Makes sure the script runs from its own directory

if [ -z "$1" ]; then
  echo "Usage: bash generate_folder_tree.sh <folder_name>"
  exit 1
fi

FOLDER=$1
OUTPUT="tree_${FOLDER}.txt"

echo "Generating tree for folder '$FOLDER'..."
python generate_tree.py "$FOLDER" > "$OUTPUT"
echo "Done! Output saved to $OUTPUT"
