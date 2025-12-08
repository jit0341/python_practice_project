# 📦 Dependencies:
# pip install schedule pandas beautifulsoup4 requests pyautogui watchdog

# ==============================================================================
# All necessary imports
# ==============================================================================
import schedule
import time
from datetime import datetime
import pandas as pd
import shutil
import os
import requests
from bs4 import BeautifulSoup
import subprocess

import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configure basic logging to see script output and debug information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# ==============================================================================
# 1. 01_schedule_task.py — Schedule recurring tasks with logging.
#    Replaces cron jobs.
# ==============================================================================
def scheduled_task_with_logging():
    """A task that runs and logs its execution time."""
    logging.info("Running scheduled task...")
    # This is where you would put the core logic of your recurring job.
    # For example, calling a backup function or a cleanup script.
    logging.info(f"Task completed at {datetime.now()}")

def setup_scheduler():
    """Sets up a scheduler to run a task every minute."""
    logging.info("Setting up a task to run every minute.")
    # The `schedule` library provides a very readable way to define jobs.
    # We schedule `scheduled_task_with_logging` to run every minute.
    schedule.every().minute.do(scheduled_task_with_logging)
    print("Scheduler is running. Press Ctrl+C to stop.")
    
    # This loop keeps the script running and checks for pending jobs every second.
    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except KeyboardInterrupt:
            logging.info("Scheduler stopped by user.")
            break

# ==============================================================================
# 2. 02_log_parser_pandas.py — Parse and analyze log files with Pandas.
#    Replaces `grep | awk | sort | uniq`.
# ==============================================================================
def create_dummy_log_file(filename="access.log"):
    """Creates a dummy log file for demonstration."""
    log_content = [
        '192.168.1.1 - [10/Aug/2025:08:00:00 +0000] "GET /home HTTP/1.1" 200 1234',
        '192.168.1.2 - [10/Aug/2025:08:00:05 +0000] "GET /about HTTP/1.1" 200 567',
        '192.168.1.1 - [10/Aug/2025:08:00:10 +0000] "GET /contact HTTP/1.1" 404 150',
        '192.168.1.3 - [10/Aug/2025:08:00:15 +0000] "POST /login HTTP/1.1" 200 200',
        '192.168.1.1 - [10/Aug/2025:08:00:20 +0000] "GET /home HTTP/1.1" 200 1234',
        '192.168.1.4 - [10/Aug/2025:08:00:25 +0000] "GET /nonexistent HTTP/1.1" 404 150',
    ]
    with open(filename, "w") as f:
        for line in log_content:
            f.write(line + "\n")
    logging.info(f"Dummy log file '{filename}' created.")

def parse_logs_with_pandas(log_file="access.log"):
    """Parses a log file and analyzes it using pandas."""
    try:
        # Create a pandas DataFrame from the log file, reading each line
        # as a separate entry. We'll use a regex to parse the different parts.
        log_df = pd.read_csv(
            log_file,
            sep=r'\s+',  # Separator is one or more whitespace characters
            header=None,
            names=['ip_address', 'column2', 'column3', 'timestamp', 'timezone',
                   'method', 'path', 'protocol', 'status_code', 'size'],
            engine='python', # The 'python' engine supports more complex regexes
        )

        # Count the number of 404 errors and group by IP address
        not_found_errors = log_df[log_df['status_code'] == 404]
        # Count the occurrences of each IP address in the filtered data
        ip_counts = not_found_errors['ip_address'].value_counts()
        
        logging.info("404 errors by IP address:")
        logging.info(ip_counts)

        # This is a much cleaner and more powerful way to analyze data
        # compared to a long chain of Bash commands.

    except FileNotFoundError:
        logging.error(f"Log file '{log_file}' not found.")
    except Exception as e:
        logging.error(f"An error occurred while parsing logs: {e}")

# ==============================================================================
# 3. 03_file_backup.py — Copy files based on filters.
#    Replaces `find /source -name "*.txt" -exec cp {} /destination \;`.
# ==============================================================================
def backup_files(source_dir, dest_dir, file_extension=".txt"):
    """Copies files with a specific extension from source to destination."""
    logging.info(f"Starting backup from '{source_dir}' to '{dest_dir}'...")
    
    # Create the destination directory if it doesn't exist
    os.makedirs(dest_dir, exist_ok=True)
    
    # Iterate through all files in the source directory
    for filename in os.listdir(source_dir):
        # Construct the full path for both source and destination
        source_path = os.path.join(source_dir, filename)
        dest_path = os.path.join(dest_dir, filename)
        
        # Check if it's a file and has the specified extension
        if os.path.isfile(source_path) and filename.endswith(file_extension):
            try:
                # Use `shutil.copy2` to copy the file, preserving metadata
                shutil.copy2(source_path, dest_path)
                logging.info(f"Copied: {source_path} -> {dest_path}")
            except Exception as e:
                logging.error(f"Failed to copy {source_path}: {e}")
    logging.info("Backup complete.")

# ==============================================================================
# 4. 04_web_scraper.py — Extract links from a webpage.
#    Replaces `curl | grep 'href' | ...`.
# ==============================================================================
def scrape_links_from_url(url="https://www.python.org"):
    """Fetches a webpage and extracts all links."""
    logging.info(f"Fetching links from: {url}")
    try:
        # Use `requests` to get the content of the page
        response = requests.get(url, timeout=10)
        # Raise an exception for bad status codes (4xx, 5xx)
        response.raise_for_status() 
        
        # Use `BeautifulSoup` to parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all `<a>` (anchor) tags in the parsed HTML
        links = [a.get('href') for a in soup.find_all('a')]
        
        # Print the extracted links
        logging.info(f"Found {len(links)} links:")
        for link in links[:10]: # Print first 10 for brevity
            print(link)
            
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch the URL: {e}")
    except Exception as e:
        logging.error(f"An error occurred during scraping: {e}")

# ==============================================================================
# 5. 05_subprocess_example.py — Run shell commands inside Python.
#    Replaces the need for a separate Bash script.
# ==============================================================================
def run_shell_command_in_python(command="ls -la"):
    """Runs a shell command and captures its output."""
    logging.info(f"Executing shell command: '{command}'")
    try:
        # `subprocess.run` is the recommended way to run shell commands.
        # `capture_output=True` captures stdout and stderr.
        # `text=True` decodes the output to a string.
        # `shell=True` allows us to pass the command as a single string.
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            shell=True,
            check=True # Raise an exception if the command returns a non-zero exit code
        )
        
        logging.info("Command stdout:")
        print(result.stdout)
        
        if result.stderr:
            logging.warning("Command stderr:")
            print(result.stderr)
            
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed with exit code {e.returncode}: {e.stderr}")
    except FileNotFoundError:
        logging.error("The command could not be found.")

# ==============================================================================
# 6. 06_api_request.py — Fetch data from APIs.
#    Replaces `curl -s 'api.url' | jq '.some.path'`.
# ==============================================================================
def fetch_api_data(api_url="https://api.github.com/users/github"):
    """Fetches JSON data from an API and processes it."""
    logging.info(f"Fetching data from API: {api_url}")
    try:
        # Use `requests.get` to make a GET request to the API
        response = requests.get(api_url, timeout=10)
        response.raise_for_status() # Check for HTTP errors
        
        # `response.json()` automatically parses the JSON response into a Python dictionary
        data = response.json()
        
        # Now you can access the data just like a Python dictionary
        username = data.get('login', 'N/A')
        public_repos = data.get('public_repos', 'N/A')
        
        logging.info("Successfully fetched API data:")
        logging.info(f"  Username: {username}")
        logging.info(f"  Public Repos: {public_repos}")
        
    except requests.exceptions.RequestException as e:
        logging.error(f"API request failed: {e}")
    except Exception as e:
        logging.error(f"An error occurred while processing API data: {e}")

# ==============================================================================
# 7. 07_gui_automation.py — Automate mouse and keyboard actions.
#    Replaces manual repetitive tasks.
# ==============================================================================
def automate_gui_task():
    """Automates a simple GUI task using pyautogui."""
    # move the import here so it's only loaded when this function is called.'
import pyautogui
logging.info("Starting GUI automation in 5 seconds. Please don't touch the mouse or keyboard.")
    # Give the user a few seconds to move their mouse away from the target window
time.sleep(5)
    
try:
        # Get the current mouse position as a reference
        x, y = pyautogui.position()
        logging.info(f"Current mouse position: ({x}, {y})")
        
        # Move the mouse to a specific coordinate
        pyautogui.moveTo(100, 150, duration=1)
        
        # Click the mouse
        pyautogui.click()
        
        # Type some text
        pyautogui.write("Hello, PyAutoGUI!", interval=0.1)
        
        # Press a keyboard key (e.g., Enter)
        pyautogui.press('enter')
        
        logging.info("GUI automation task completed.")
        
except pyautogui.FailSafeException:
        # PyAutoGUI's failsafe is a great safety feature
        logging.error("GUI automation failed. Mouse was moved to a corner. Script aborted.")
except Exception as e:
        logging.error(f"An error occurred during GUI automation: {e}")

# ==============================================================================
# 8. 08_folder_watcher.py — Detect file changes in a folder.
#    Replaces a polling script (`while true; do ...`).
# ==============================================================================
class MyEventHandler(FileSystemEventHandler):
    """Custom event handler to react to file system events."""
def on_created(self, event):
        """Called when a file or directory is created."""
        if not event.is_directory:
            logging.info(f"New file created: {event.src_path}")
            # Add your custom action here, e.g., backup_new_file(event.src_path)

def on_deleted(self, event):
        """Called when a file or directory is deleted."""
        if not event.is_directory:
            logging.info(f"File deleted: {event.src_path}")

def watch_folder(folder_path="."):
    """Sets up a folder watcher to monitor for file changes."""
    logging.info(f"Watching folder '{folder_path}'. Press Ctrl+C to stop.")
    
    # Create an event handler instance
    event_handler = MyEventHandler()
    # Create an observer instance
    observer = Observer()
    
    # Schedule the observer to watch the specified path, recursively
    observer.schedule(event_handler, folder_path, recursive=True)
    
    # Start the observer in a separate thread
    observer.start()
    
try:
        # Keep the main thread alive until a KeyboardInterrupt (Ctrl+C)
        while True:
            time.sleep(1)
except KeyboardInterrupt:
        # Stop the observer gracefully
        observer.stop()
        logging.info("Folder watcher stopped.")
    
observer.join() # Wait for the observer thread to finish

# ==============================================================================
# Main execution block to run all examples
# ==============================================================================
if __name__ == "__main__":
    print("Welcome to your Python Automation Examples!")
    print("===========================================")

    # Create a simple project structure for demonstration
    os.makedirs("source_files", exist_ok=True)
    with open("source_files/document1.txt", "w") as f: f.write("Hello, World!")
    with open("source_files/image.jpg", "w") as f: f.write("Dummy content")

    # Run each example function one by one
    
    print("\n--- Example 1: Scheduled Task ---")
    # This example requires a continuous loop to run.
    # To avoid this, we'll run a single instance of the task instead of the full scheduler.
    logging.info("Note: The full scheduler runs in a loop. We'll run one instance for this demo.")
    scheduled_task_with_logging()

    print("\n--- Example 2: Log Parser ---")
    create_dummy_log_file()
    parse_logs_with_pandas()

    print("\n--- Example 3: File Backup ---")
    backup_files("source_files", "backup_files")

    print("\n--- Example 4: Web Scraper ---")
    scrape_links_from_url()

    print("\n--- Example 5: Subprocess ---")
    run_shell_command_in_python("echo 'Hello from the shell!'")

    print("\n--- Example 6: API Request ---")
    fetch_api_data()

    print("\n--- Example 7: GUI Automation ---")
    # Note: GUI automation can be disruptive.
    # It's commented out by default to prevent unexpected behavior.
    # Uncomment the next line to run it.
    # automate_gui_task()
    logging.info("GUI automation is commented out. Uncomment 'automate_gui_task()' to run.")

    print("\n--- Example 8: Folder Watcher ---")
    logging.info("Note: The folder watcher will run until you press Ctrl+C.")
    # watch_folder("source_files")
    logging.info("Folder watcher is commented out. Uncomment 'watch_folder()' to run.")

    print("\nAll examples (except the continuous ones) have finished.")
    print("You can now modify and run each function individually!")



