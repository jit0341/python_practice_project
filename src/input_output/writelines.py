lines = ["Apple\n", "Banana\n", "Cherry\n","Mango\n"]
with open("fruits.txt", "w") as f:
    f.writelines(lines)
    
   from project_utils.save_to_txt import save_data_as_log

info = {
    "Name": "Jitendra",
    "Age": 48,
    "Language": "Python",
    "Goal": "Freelancing"
}

save_data_as_log("my_profile.txt", info)