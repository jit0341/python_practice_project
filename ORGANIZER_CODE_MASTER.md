📁 FILE 2 — ORGANIZER_CODE_MASTER.md
(Pure code + technical reasoning)
Use this file to master HOW + LOGIC.
📂 Folder File Organizer — Python Code & Logic
🔧 Imports
Copy code
Python
import os
import shutil
os → filesystem navigation
shutil → safe file movement
No external dependencies.
⚙️ Configuration Section
Copy code
Python
BASE_PATH = os.getcwd()

DRY_RUN = False
OVERWRITE = False
Purpose
BASE_PATH dynamically targets the current folder
DRY_RUN enables preview mode
OVERWRITE prevents accidental file replacement
These flags make the script safe and client-friendly.
🗂 File Type Rules
Copy code
Python
FILE_TYPES = {
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Audio": [".mp3"]
}
Business rules are separated from logic for easy customization.
📊 Counters (Reporting)
Copy code
Python
total_files = 0
moved_files = 0
skipped_files = 0
Used for clear execution summary.
🔄 Main Processing Loop
Copy code
Python
for item in os.listdir(BASE_PATH):
Iterates through all items in the target folder.
✅ Validation Logic
Copy code
Python
if not os.path.isfile(item_path):
    continue
Ensures only files are processed.
Copy code
Python
if item == "organizer.py":
    skipped_files += 1
    continue
Prevents self-movement.
Copy code
Python
if item.startswith("."):
    skipped_files += 1
    continue
Skips hidden/system files.
🧠 Decision Logic (Business Rules)
Copy code
Python
name, ext = os.path.splitext(item)
Extracts file extension for classification.
Each extension is matched against predefined categories.
📂 Folder Creation & File Movement
Copy code
Python
os.makedirs(folder_path, exist_ok=True)
Creates folders safely if missing.
Copy code
Python
shutil.move(item_path, destination)
Moves files efficiently.
Overwrite checks prevent data loss.
📁 Others Category Handling
Files that don’t match any category are sent to an Others folder using the same safety logic.
📈 Summary Report
Copy code
Python
print(f"Total files found : {total_files}")
print(f"Files moved       : {moved_files}")
print(f"Files skipped     : {skipped_files}")
Provides clear execution feedback.
🧠 Key Python Concepts Used
File handling (os, shutil)
Loops
Dictionaries
Conditional logic
Defensive programming
Modular configuration design
🔁 Reusability Insight
This script can be adapted for:
Image compressors
Log file cleanup
Backup automation
Client-specific workflows
🎯 Mastery Goal
You have mastered this project when you can:
Explain it without code
Modify rules confidently
Rebuild it from scratch
Teach it to someone else
