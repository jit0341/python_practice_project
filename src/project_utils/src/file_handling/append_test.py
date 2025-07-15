with open("myfile.txt", "a") as f:
    f.write("This line is appended.\n")
    f.write("Jitendra is learning Python file handling.\n")
   
  # Date and time 
    from datetime import datetime

with open("log.txt", "a") as f:
    now = datetime.now()
    f.write(f"[{now}] Jitendra completed append mode.\n")
    
  # List 
    
    lines = ["Apple\n", "Banana\n", "Cherry\n","Mango\n"]
with open("fruits.txt", "w") as f:
    f.writelines(lines)
    
   # Quiz
    score = 3
total = 5
name = input("Enter your name: ")

with open("quiz_scores.txt", "a") as f:
    f.write(f"{name} scored {score}/{total}\n")
    
 # try-except while writing
 
data = "This is safe writing.\n"

try:
    with open("write_test.txt", "a") as f:
        f.write(data)
except PermissionError:
    print("❌ You don’t have permission to write to this file.")
else:
    print("✅ Data written successfully.")
finally:
    print("📦 Write attempt complete.")
    
# General-purpose save_log()  Function

def save_log(text, filename="log.txt"):
    try:
        with open(filename, "a") as f:
            f.write(text + "\n")
    except Exception as e:
        print(f"❌ Failed to save log: {e}")
    else:
        print("✅ Log saved successfully.")

save_log("Jitendra started file handling practice.")

save_log("User Jitendra completed file writing lesson.")

save_log("Day 2: Learned file writing with 'a' mode", "daily_log.txt")