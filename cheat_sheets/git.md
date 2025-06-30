

# 🧠 Git Cheat Sheet — Essentials for Daily Use

## 🔧 Repository Setup
| Task                        | Command                                     |
|-----------------------------|---------------------------------------------|
| Initialize repo             | `git init`                                  |
| Link to remote              | `git remote add origin <repo-url>`          |
| Rename branch to main       | `git branch -M main`                        |

## 🔄 Status, Add, Commit
| Task                        | Command                                     |
|-----------------------------|---------------------------------------------|
| Check status                | `git status`                                |
| Stage all changes           | `git add .` or `git add --all`             |
| Commit with message         | `git commit -m "your message"`              |

## 🚀 Push & Pull
| Task                        | Command                                     |
|-----------------------------|---------------------------------------------|
| Push to GitHub              | `git push origin main`                      |
| Pull latest changes         | `git pull origin main --rebase`            |

## 📚 History & Fixes
| Task                        | Command                                     |
|-----------------------------|---------------------------------------------|
| View commit log             | `git log --oneline`                         |
| Amend last commit message   | `git commit --amend -m "new message"`       |

> ✅ Tip: Use `git add -p` to stage only selected changes interactively.
