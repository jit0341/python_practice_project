
with open ("media_log.txt","w") as file:
    
    file.write(f"[2025-07-18 06:07] YouTube | Python tutorial | 20 min\n ")
    file.write(f"[2025-07-18 06:16] whatsapp | chat with cousin | 10 min\n ")
    file.write(f"[2025-07-18 06:20] YouTube | Python short | 4 min\n")

count = 0
with open("media_log.txt", "r") as file:
    for line in file:
        if "youtube" in line.lower():
            count += 1

print(f"YouTube entries found: {count}")


