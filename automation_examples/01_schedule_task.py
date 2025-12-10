#!/usr/bin/env python3
# 01_schedule_task.py
# Schedule recurring tasks and log their runs.

import time                       # time.sleep for loop
import logging                    # logging events to file/console
import schedule                   # lightweight scheduler library
from datetime import datetime     # timestamps

# configure basic logging to a file and to console
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("automation_schedule.log"),  # log file
        logging.StreamHandler()                          # also print to console
    ]
)

def my_task():
    """Example task function to be scheduled."""
    # create a timestamp string
    ts = datetime.utcnow().isoformat() + "Z"
    # log that the task ran
    logging.info(f"Running scheduled task at {ts}")
    # place real work here (call other functions, run backups, etc.)
    # Example placeholder:
    logging.info("Task: placeholder work done")

def setup_jobs():
    """Register scheduled jobs with the schedule module."""
    # run my_task every minute
    schedule.every(1).minutes.do(my_task)
    # run my_task at 09:00 every day (local time)
    schedule.every().day.at("09:00").do(my_task)
    # add any more jobs here

if __name__ == "__main__":
    # when run as script, set up jobs and enter the loop
    logging.info("Starting scheduler...")
    setup_jobs()
    try:
        # loop forever, running pending scheduled jobs
        while True:
            schedule.run_pending()  # run any jobs ready to run
            time.sleep(1)           # sleep a little to avoid busy loop
    except KeyboardInterrupt:
        # graceful shutdown on Ctrl+C
        logging.info("Scheduler stopped by user")
