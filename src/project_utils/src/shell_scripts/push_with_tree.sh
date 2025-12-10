#!/data/data/com.termux/files/usr/bin/bash

cd ~/python_practice_project

# Step 1: Regenerate tree
./generate_folder_tree.sh

# Step 2: Git add, commit, push
git add .
git commit -m "Updated tree and files"
git push origin main
