# Databases

1. What is a database + DBMS
2. Tables, rows, columns (the relational model)
3. SQL + CRUD
4. Data modeling (entities + relationships)
5. Keys + constraints (PK, FK, UNIQUE, NOT NULL)
6. Joins

## What Is a Database?

- A database is an organized way to store data so you can reliably read/write it later.
- A DBMS (Database Management System) is software that manages:
  - saving data (persistence)
  - multiple users (concurrency)
  - rules on data (constraints)

> Quick comparison: file vs database

- Text/JSON files are simple and great for small projects.
- Databases become valuable when you need:
  - consistent structure
  - fast searching/filtering
  - multiple related “types” of data
  - rules that prevent bad data
  - reliable updates (especially if something crashes mid-save)

## Relational Databases (Tables)

- Data is stored in tables:
  - rows = individual records
  - columns = properties/fields of the record
- Common mental model:
  - A table is like a spreadsheet, but with stronger rules and better querying.

## Relational vs NoSQL (2–3 min)

- Relational DBs (SQLite, Postgres, MySQL)
  - best when your data is structured and connected
  - strong constraints + joins + transactions
- NoSQL DBs (MongoDB, Redis, DynamoDB, etc.)
  - often used for flexibility, scale, or specialized access patterns
  - different “families” (document, key-value, graph, etc)

> Rule of thumb

- If you need relationships + reporting + correctness, start relational.
- If you have a specific scale/flexibility need, pick a NoSQL type that matches the access pattern.

## SQL + CRUD

CRUD is the basic lifecycle of data:

- Create → `INSERT`
- Read → `SELECT`
- Update → `UPDATE`
- Delete → `DELETE`

### Tiny SQL examples

```sql
-- Create a table
CREATE TABLE courses (
  id   INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  term TEXT NOT NULL
);

-- Insert a row
INSERT INTO courses (name, term) VALUES ('CS 1101', 'Spring 2026');

-- Read rows
SELECT id, name, term FROM courses ORDER BY name;

-- Update a row
UPDATE courses SET term = 'Summer 2026' WHERE id = 1;

-- Delete a row
DELETE FROM courses WHERE id = 1;
```

## Data Modeling (Design Before Code)

- Entity: a “thing” you care about (Course, Grade)
- Attribute: a detail about the thing (Course.name, Grade.score)
- Relationship: how entities connect (Course has many Grades)

> Mini-prompt (2 minutes)

- If we’re building a personal gradebook, what entities do we need?
- Which attributes should be required?
- Which relationships exist?

## Keys + Constraints (How Databases Prevent Bad Data)

- Primary Key (PK): unique identifier for a row (often `id`)
- Foreign Key (FK): a reference to another table’s PK
- Constraints (rules):
  - `NOT NULL` → this field is required
  - `UNIQUE` → prevent duplicates

### Why constraints matter

- They prevent “quiet bugs” where invalid data sneaks in.
- Your app can be wrong; the database helps keep data consistent.

## Joins

Joins let you combine related tables.

```sql
-- Join grades to their course
SELECT
  c.name AS course,
  g.item,
  g.score,
  g.max_score
FROM grades g
JOIN courses c ON c.id = g.course_id
WHERE c.id = 1
ORDER BY g.id;
```

## Security + Backups (Practical Basics)

- Don’t build SQL by string concatenation.
  - Use parameterized queries (ex: `WHERE name = ?`).
- Backups matter because:
  - mistakes happen (accidental deletes)
  - devices fail
- Permissions matter (who can read/modify data?)

## SQLite + Python (What We’re Using)

- SQLite is a lightweight relational database stored in a single file.
- Great for:
  - learning SQL
  - small apps
  - prototypes
- In Python, we use the built-in `sqlite3` module.

## Activity Overview: Personal Gradebook (SQLite + Python)

- Build a console app that stores:
  - courses
  - grades per course
- Practice:
  - designing a schema
  - writing SQL
  - using Python to query/update a DB
