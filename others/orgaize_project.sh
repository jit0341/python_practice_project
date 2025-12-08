#!/data/data/com.termux/files/usr/bin/bash

# Create folders
mkdir -p src tests data media docs utils logs

# Move Python source files (core code)
mv *.py src/ 2>/dev/null

# Move test files
mv src/test_*.py tests/ 2>/dev/null
mv src/*_test.py tests/ 2>/dev/null
mv test_files_backup.zip tests/ 2>/dev/null

# Move .txt and .csv files to data
mv *.txt data/ 2>/dev/null
mv *.csv data/ 2>/dev/null
mv *.json data/ 2>/dev/null
mv *file.txt data/ 2>/dev/null

# Move media files
mv *.jpg media/ 2>/dev/null
mv *.mp3 media/ 2>/dev/null
mv *.mp4 media/ 2>/dev/null

# Move utilities
mv src/json_processor.py utils/ 2>/dev/null
mv src/create_log.py utils/ 2>/dev/null
mv src/log_*.py utils/ 2>/dev/null

# Move logs
mv src/*log*.py logs/ 2>/dev/null
mv src/*log*.txt logs/ 2>/dev/null

# Move planning, docs, learning stuff
mv *Plan*.md docs/ 2>/dev/null
mv *timetable*.xlsx docs/ 2>/dev/null
mv revisit_basics.py docs/ 2>/dev/null

echo "✅ Project organized successfully!"
