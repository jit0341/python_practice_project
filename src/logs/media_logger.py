import os
import time
source_folder = "media_files"
dest_folder = "media_backup"
log_file = "media_log.txt"

os.makedirs(dest_folder, exist_ok = True)

files = os.listdir(source_folder)
media_files = [f for f in files if 
 f.lower().endswith((".jpg", ".mp3", ".mp4"))]

for filename in media_files:
    print(f"Processing: {filename}")
    src_path = os.path.join(source_folder,filename)
    dest_path = os.path.join(dest_folder,filename)
    
    with open(src_path, "rb") as src_file:
        data = src_file.read()

    with open(dest_path,"wb") as dest_file:
        dest_file.write(data)

    size_kb = os.path.getsize(dest_path)/1024
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"{filename} | {round(size_kb,2)} KB | Copied at {timestamp}\n"
    with open(log_file, "a") as log:
        log.write(log_line)

        print("All media files copied and logged.")

def show_summary ():
    total = 0
    summary = {}
    with open ("media_log.txt","r") as f:
        for line in f:
            line = line.strip()
            if ":" in line:
                name,minutes = line.split(":") 
                name = name.strip()
                minutes = int(minutes.strip())
                total += minutes
                if name in summary:
                    summary[name] += minutes
                else:
                    summary[name] = minutes
    print(f"Media Usage Summary:\n-----------------")
    for platform,mins in  summary.items():
        print(f"{platform}: {min} minutes")
        print(f"Total time: {total} minutes")

        # Uncomment below line to test the summary
    show_summary()

