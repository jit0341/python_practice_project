# create_log.py

log_content = """INFO: Application started successfully.
DEBUG: Initializing database connection.
INFO: User 'Alice' logged in.
ERROR: Failed to connect to external API. Retrying...
DEBUG: Processing user request ID: 12345.
INFO: Data saved to disk.
ERROR: Disk space low. Cannot write new data.
WARN: High CPU usage detected.
INFO: Application shutting down.
ERROR: Unhandled exception occurred in module X.
"""

# Open the file in write mode ('w'). If it exists, it will be overwritten.
# If it doesn't exist, it will be created.
try:
    with open("app_log.txt", "w") as file:
        file.write(log_content)
    print("app_log.txt created successfully.")
except IOError as e:
    print(f"Error creating file: {e}")

