✅ 3. Termux-Specific: Daily Use Cheat Sheet
Task	Command
```
Update pkg	pkg update && pkg upgrade
Install package	pkg install <name> (e.g., pkg install git)
List files/folders	ls, ls -a, ls -l
Create file/folder	touch file.py, mkdir foldername
Move/Rename file	mv oldname newname
Run Python script	python file.py
Run bash script	bash script.sh or ./script.sh
Make bash script executable	chmod +x script.sh
Navigate folders	cd foldername, cd .., pwd
Git push (short)	git add . && git commit -m "msg" && git push

```


---

### 📄 `cheat_sheets/termux.md`

```markdown
# 🖥️ Termux Cheat Sheet — Daily CLI Use

## 📦 Package Management
| Task                          | Command                                  |
|-------------------------------|------------------------------------------|
| Update pkg                    | `pkg update && pkg upgrade`              |
| Install package               | `pkg install <name>`                     |

## 🗂️ File & Directory
| Task                          | Command                                  |
|-------------------------------|------------------------------------------|
| List files                    | `ls`, `ls -l`, `ls -a`                    |
| Create folder                 | `mkdir foldername`                       |
| Create file                   | `touch filename.py`                      |
| Navigate                      | `cd folder`, `cd ..`, `pwd`              |
| Move/rename file              | `mv oldname newname`                     |
| Delete file                   | `rm filename`                            |

## 🐍 Run Scripts
| Task                          | Command                                  |
|-------------------------------|------------------------------------------|
| Run Python script             | `python script.py`                       |
| Run Bash script               | `bash script.sh` or `./script.sh`        |
| Make Bash script executable   | `chmod +x script.sh`                     |

## 🌐 GitHub via Termux
| Task                          | Command                                  |
|-------------------------------|------------------------------------------|
| Add & commit                  | `git add . && git commit -m "msg"`       |
| Push                          | `git push origin main`                   |
| Pull                          | `git pull origin main --rebase`          |
