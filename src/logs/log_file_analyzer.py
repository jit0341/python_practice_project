# log_file_analyzer.py

total_log_entries = 0
error_entries = 0
error_lines = [] # To store the error lines before writing them to a new file

# --- Phase 2: Read and Process app_log.txt ---
try:
    with open("app_log.txt", "r") as log_file:
        for line in log_file: # Read file line by line (memory efficient)
            total_log_entries += 1
            if "ERROR" in line: # Check if "ERROR" is present in the line
                error_entries += 1
                error_lines.append(line.strip()) # Add the line (stripped of newline) to our list
                # .strip() removes leading/trailing whitespace, including newline characters
                # We'll add the newline back when writing to error_report.txt

except FileNotFoundError:
    print("Error: app_log.txt not found. Please ensure it's in the same directory.")
    exit() # Exit the script if the log file isn't found
except IOError as e:
    print(f"An error occurred while reading app_log.txt: {e}")
    exit()

# --- Phase 3: Generate Error Report and Print Summary ---

# Open error_report.txt in write mode ('w')
try:
    with open("error_report.txt", "w") as report_file:
        for error_line in error_lines:
            report_file.write(error_line + "\n") # Add newline back for file formatting
    print("Error report generated: error_report.txt")
except IOError as e:
    print(f"An error occurred while writing to error_report.txt: {e}")

# Print summary to console
print(f"Total log entries: {total_log_entries}")
print(f"Total error entries: {error_entries}")



