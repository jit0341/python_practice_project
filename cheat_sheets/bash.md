
---

📄 cheat_sheets/bash.md

# 🐚 Bash Cheat Sheet — Simple Scripting & Commands

## 🛠️ File Operations

| Task                  | Command                                 |
|-----------------------|-----------------------------------------|
| List files            | `ls`, `ls -l`, `ls -a`                  |
| Create file           | `touch file.txt`                        |
| Create folder         | `mkdir my_folder`                       |
| Rename file/folder    | `mv old.txt new.txt`                    |
| Delete file           | `rm file.txt`                           |
| Delete folder         | `rm -r folder_name


| View file content     | `cat file.txt`                          |
| Edit file (basic)     | `nano file.sh`                          |

---

## 🧮 Variables

```bash
name="Jitendra"
echo "Hello, $name"


---

🔁 Loops

➤ For Loop

for i in 1 2 3; do
  echo "Number: $i"
done

➤ Loop over files

for file in *.txt; do

echo "Found file: $file"
done


---

🔍 Conditions

if [ -f file.txt ]; then
  echo "File exists"
else
  echo "File not found"
fi


---

⚙️ Permissions

Task	Command

Make script executable	chmod +x script.sh
Run script	./script.sh
Run with bash	bash script.sh



---
🧰 Custom Script Template

#!/data/data/com.termux/files/usr/bin/bash
echo "This is a script!"

✅ Always start with #!/bin/bash or the full Termux path above.


---

💡 Helpful Commands

Purpose	Command

Print current dir	pwd
Go to folder	cd foldername
Back one dir	cd ..
Show current user	whoami



---

🔄 Git + Bash Combo

Automate Git pushes:

#!/bin/bash
cd ~/python_practice_project
git add .
git commit -m "Auto update"
git push origin main

Save this as push_all.sh, make it executable, and run it in 1 command!


---

📘 Tips

Use # for comments

Use && to chain commands: mkdir test && cd test

Use sleep 2 to delay


---

### ✅ What to Do Now

1. Open:
   ```bash
   nano cheat_sheets/bash.md

