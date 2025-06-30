
# 🧮 SQL Cheat Sheet — Beginner Essentials

---

## 📁 Table Operations

| Task                        | Command Example                                  |
|-----------------------------|--------------------------------------------------|
| Create a table              | `CREATE TABLE students (id INT, name TEXT);`     |
| View table structure        | `PRAGMA table_info(students);`                  |
| Drop a table                | `DROP TABLE students;`                           |
| Rename a table              | `ALTER TABLE old_name RENAME TO new_name;`       |

---

## 📥 Insert, Read, Update, Delete (CRUD)

| Action     | Syntax Example |
|------------|----------------|
| Insert     | `INSERT INTO students VALUES (1, 'Anita');` |
| Select     | `SELECT * FROM students;` |
| Update     | `UPDATE students SET name = 'Aman' WHERE id = 1;` |
| Delete     | `DELETE FROM students WHERE id = 1;` |

---

## 🎯 Filtering Data

| Task                  | Command Example |
|-----------------------|-----------------|
| Where clause          | `SELECT * FROM students WHERE name = 'Aman';` |
| Comparison            | `WHERE marks >= 50` |
| AND / OR              | `WHERE age > 18 AND class = 9` |
| IN clause             | `WHERE subject IN ('Math', 'Science')` |
| BETWEEN               | `WHERE marks BETWEEN 50 AND 80` |
| IS NULL               | `WHERE email IS NULL` |

---

## 🔢 Sorting & Limiting

| Task              | Syntax Example |
|-------------------|----------------|
| Order ascending   | `ORDER BY name ASC` |
| Order descending  | `ORDER BY marks DESC` |
| Limit rows        | `LIMIT 5` |
| Offset (skip)     | `LIMIT 5 OFFSET 5` |

---

## 🔁 Joins (Basic)

| Type      | Example |
|-----------|---------|
| INNER JOIN | `SELECT * FROM A INNER JOIN B ON A.id = B.id;` |
| LEFT JOIN  | `SELECT * FROM A LEFT JOIN B ON A.id = B.id;` |
| RIGHT JOIN | *Not in SQLite* |
| FULL OUTER | *Not in SQLite* |

---

## 🧠 Functions

| Type         | Example |
|--------------|---------|
| Count rows   | `SELECT COUNT(*) FROM students;` |
| Average      | `SELECT AVG(marks) FROM students;` |
| Maximum      | `SELECT MAX(age) FROM students;` |
| Minimum      | `SELECT MIN(age) FROM students;` |
| Sum          | `SELECT SUM(fees) FROM students;` |

---

## 📌 Grouping & Aggregation

```sql
SELECT class, COUNT(*) 
FROM students 
GROUP BY class 
HAVING COUNT(*) > 5;


---

🔐 Constraints

Type	Example

Primary Key	id INT PRIMARY KEY
Not Null	name TEXT NOT NULL
Unique	email TEXT UNIQUE
Default	status TEXT DEFAULT 'active'



---

🔎 Wildcards & LIKE

Pattern	Matches

%a%	contains 'a'
a%	starts with 'a'
%a	ends with 'a'
_a_	3-letter words with 'a' in middle


SELECT * FROM users WHERE name LIKE 'A%';


Use ; at the end of every SQL command when working in SQL shells or scripts.

---

