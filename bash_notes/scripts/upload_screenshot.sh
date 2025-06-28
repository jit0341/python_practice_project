#!/data/data/com.termux/files/usr/bin/bash

# Step 1: Ask for new file name
echo "Enter new file name (without .jpg): "
read newname

# Step 2: Find the latest screenshot
latest_screenshot=$(ls -t ~/storage/pictures/Screenshots/*.jpg | head -n 1)

# Step 3: Check if file found
if [ ! -f "$latest_screenshot" ]; then
  echo "No screenshot found!"
  exit 1
fi

# Step 4: Move and rename
destination=~/python_practice_project/sql_notes/screenshots/${newname}.jpg
mv "$latest_screenshot" "$destination"

# Step 5: Git add, commit, push
cd ~/python_practice_project
git add "$destination"
git commit -m "Added screenshot: ${newname}"
git push origin main

echo "✅ Screenshot uploaded and pushed to GitHub."
