import os
import time
import schedule
import toolbox
from datetime import datetime

SOURCE_FOLDER = "../src"
BACKUP_FOLDER = "../backups"

def get_timestamped_name():
    today = datetime.now().strftime("%Y-%m-%d_%H-%M")
    return f"python_backup_{today}.zip"

def check_for_changes():
    # Check if any file in src/ has been changed today
    for root, dirs, files in os.walk(SOURCE_FOLDER):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                if time.time() - os.path.getmtime(path) < 24 * 3600:  # changed in last 24 hrs
                    return True
    return False

def auto_zip_if_changed():
    if check_for_changes():
        print("📌 Changes detected! Backing up...")
        os.makedirs(BACKUP_FOLDER, exist_ok=True)
        zip_name = os.path.join(BACKUP_FOLDER, get_timestamped_name())
        toolbox.zip_folder(SOURCE_FOLDER, zip_name)
        print(f"✅ Backup created: {zip_name}")
    else:
        print("🟡 No recent changes. Skipping backup.")

# Schedule: once daily at 8 PM
schedule.every().day.at("20:00").do(auto_zip_if_changed)

print("⏳ Daily auto-backup scheduled at 8:00 PM. Press Ctrl+C to exit.")

while True:
    schedule.run_pending()
    time.sleep(60)
