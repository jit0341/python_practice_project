
<pre>
# 🧰 Workflow Summary: SQL + GitHub (Day 2)

This file documents every step followed while working with SQL queries, screenshots, markdown, and GitHub.

---

## 🗂️ Folder Structure

```bash
python_practice_project/
├── sql_notes/
│   ├── day1_intro.md
│   ├── day2_filtering_sorting.md
│   ├── screenshots/
│   │   ├── where_query_germany.jpg
│   │   ├── or_query_germany_mexico.jpg
│   │   └── ...
│   └── README.md
├── python_notes/
│   └── ...
├── workflow_summary.md
├── README.md
└── .gitignore
```

---

## ✅ Daily Workflow Steps

### 1. Write SQL Query
Example:
```sql
SELECT * FROM Customers WHERE Country = 'Germany';
```

### 2. Take Screenshot of Output  
Save to: `/storage/emulated/0/Pictures/Screenshots/`

### 3. Rename Screenshot
```bash
mv Screenshot_xxx.jpg where_query_germany.jpg
```

### 4. Move to Project Screenshot Folder
```bash
mv where_query_germany.jpg ~/python_practice_project/sql_notes/screenshots/
```

### 5. Add to `.md` Notes
Inside `day2_filtering_sorting.md`:
```markdown
```sql
SELECT * FROM Customers WHERE Country = 'Germany';
```
![Output](./screenshots/where_query_germany.jpg)
```

---

## 📤 GitHub Workflow

```bash
git status
git add .
git commit -m "Add Day 2 SQL queries and screenshots"
git push origin main
```

---

## 🌳 Tree Command to Show Structure
```bash
tree -L 2 > tree_sql_notes.txt
```

Use content of this file in README.md inside `sql_notes/`.

---

## 🧹 Extra Commands

- Delete mistaken file:
```bash
rm sql_notes/old_file.md
```

- Go back one folder:
```bash
cd ..
```
</pre>
---

💾 4. Save and Exit:

Ctrl + O → Enter

Ctrl + X → Exit



---

📤 5. Commit and Push to GitHub:

git add workflow_summary.md
git commit -m "Add workflow summary for SQL + GitHub"
git push origin main


---

