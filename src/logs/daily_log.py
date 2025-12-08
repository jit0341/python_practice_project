import os
from datetime import datetime

# Create folder for daily logs
LOG_FOLDER = os.path.join(os.path.dirname(__file__), "daily_logs")
os.makedirs(LOG_FOLDER, exist_ok=True)

# Get today's filename
today = datetime.now().strftime("%Y-%m-%d")
filename = f"{today}_log.txt"
filepath = os.path.join(LOG_FOLDER, filename)

print(f"\nToday's log file: {filename}")
print("Type your entry below.")
print("Type 'r' to review today's log, 'r all' to see all logs, or 'exit' to quit.\n")

# Function to write entry with timestamp
def write_entry(entry):
    timestamp = datetime.now().strftime("%H:%M")
    with open(filepath, "a") as f:
        f.write(f"[{timestamp}] {entry.strip()}\n")

# Function to show today’s log
def show_today_log():
    if os.path.exists(filepath):
        print("\n📝 Today's Log:\n" + "-" * 30)
        with open(filepath, "r") as f:
            print(f.read())
    else:
        print("No log found for today.")

# Function to show all logs
def show_all_logs():
    print("\n📚 All Logs:\n" + "-" * 30)
    for file in sorted(os.listdir(LOG_FOLDER)):
        print(f"\n📅 {file}")
        with open(os.path.join(LOG_FOLDER, file), "r") as f:
            print(f.read())

# Main input loop
while True:
    entry = input("➤ ")
    if entry.lower() == "exit":
        print("Log saved. Exiting...")
        break
    elif entry.lower() == "r":
        show_today_log()
    elif entry.lower() == "r all":
        show_all_logs()
    elif entry.strip() != "":
        write_entry(entry)
    else:
        print("Empty input. Try again.")
