# Activity: SQLite Gradebook (Python Console App)

## Goal

Build a console app that stores your **courses** and **grades** in an SQLite database file.

By the end you should be able to:

- Insert and query data with SQL
- Use Python’s `sqlite3` module with parameterized queries
- Generate a simple “report” (course average)

## What You’re Building

A program that runs in the terminal and lets you:

1. Add a course
2. List courses
3. Add a grade for a course
4. View a course report (all grades + average)

## Requirements

- Use Python + the built-in `sqlite3` library (no extra packages)
- Store data in `gradebook.db` (SQLite file)
- Use **two tables** with a relationship:
  - `courses`
  - `grades` (with a foreign key to `courses`)
- Use **parameterized SQL** (`?` placeholders) for user input

## Setup

- Open the starter file: `sqlite-gradebook/gradebook.py`
- Run it

## Schema

- `courses`
  - `id` (PK)
  - `name` (TEXT, required)
  - `term` (TEXT, required)
- `grades`
  - `id` (PK)
  - `course_id` (FK → courses.id)
  - `item` (TEXT, required)
  - `score` (REAL, required)
  - `max_score` (REAL, required)

## Step-by-Step Tasks

### Add and list courses

1. Implement `add_course(conn)`
   - Prompt for `name` and `term`
   - Insert the row
2. Implement `list_courses(conn)`
   - Query all courses
   - Print them with their `id`

### Add grades

1. Implement `add_grade(conn)`
   - Let the user pick a course (by id)
   - Prompt for:
     - assignment/item name
     - score earned
     - max score
   - Insert into `grades`

### Course report

Implement `course_report(conn)`:

- Show all grades for a course
- Compute average percent:

$$\text{percent} = 100 \times \frac{\sum score}{\sum max\_score}$$

Tip: use a JOIN to display course name, and use SUM() for totals.

## Checkpoint: Minimum Working App

Your app is “done” when:

- It creates the database and tables
- You can add at least 2 courses
- You can add at least 3 grades across courses
- You can view a report showing:
  - all grades for a course
  - average percent for that course

## Stretch Goals (If You Finish Early)

- Add “delete course” (and cascade delete its grades)
- Add “update grade”
- Add “overall GPA” using a simple scale (ex: A=4, B=3, ...)
- Add “search courses” by keyword
