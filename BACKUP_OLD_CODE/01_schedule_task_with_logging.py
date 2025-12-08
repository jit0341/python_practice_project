import schedule
import time
from datetime import datetime
import logging

# ---------------- Logging Setup ----------------
logging.basicConfig(
    filename="example.log",           # Log file name
    level=logging.INFO,               # Log only INFO and above
    format="%(asctime)s [%(levelname)s] %(message)s",  # Log format
    datefmt="%Y-%m-%d %H:%M:%S,%f"     # Time format
)

# ---------------- Task Function ----------------
def job():
    logging.info("Running scheduled task")
    # Simulate doing some work
    try:
        result = "Task completed successfully"
        logging.info(f"Task result: {result}")
    except Exception as e:
        logging.error(f"Task failed: {e}")

# ---------------- Schedule Setup ----------------
schedule.every(5).seconds.do(job)  # Run every 5 seconds

logging.info("Scheduler started")

# ---------------- Main Loop ----------------
while True:
    schedule.run_pending()
    time.sleep(1)
