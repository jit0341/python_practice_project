#!/data/data/com.termux/files/usr/bin/bash

# Set target folder
TARGET_DIR=~/storage/shared/python_practice_project

# Create subfolders
mkdir -p "$TARGET_DIR/src"
mkdir -p "$TARGET_DIR/data"
mkdir -p "$TARGET_DIR/media"
mkdir -p "$TARGET_DIR/tests"
mkdir -p "$TARGET_DIR/others"

# Move Python scripts
find "$TARGET_DIR" -maxdepth 1 -type f -name "*.py" -exec mv {} "$TARGET_DIR/src/" \;

# Move test files
find "$TARGET_DIR" -maxdepth 1 -type f -name "test_*.py" -exec mv {} "$TARGET_DIR/tests/" \;

# Move data files
find "$TARGET_DIR" -maxdepth 1 -type f \( -name "*.csv" -o -name "*.tsv" -o -name "*.json" \) -exec mv {} "$TARGET_DIR/data/" \;

# Move media files
find "$TARGET_DIR" -maxdepth 1 -type f \( -iname "*.jpg" -o -iname "*.png" -o -iname "*.mp4" \) -exec mv {} "$TARGET_DIR/media/" \;

# Move other files
find "$TARGET_DIR" -maxdepth 1 -type f ! -path "$TARGET_DIR/*.py" ! -path "$TARGET_DIR/*.csv" ! -path "$TARGET_DIR/*.json" ! -path "$TARGET_DIR/*.tsv" ! -iname "*.jpg" ! -iname "*.png" ! -iname "*.mp4" ! -name "organize_project.sh" -exec mv {} "$TARGET_DIR/others/" \;

echo "✅ Project organized successfully!"
