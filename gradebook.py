import sqlite3
from dataclasses import dataclass
from pathlib import Path

DB_PATH = Path(__file__).with_name("gradebook.db")


def get_connection(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    # Required in SQLite: foreign keys are OFF by default
    conn.execute("PRAGMA foreign_keys = ON;")

    return conn


def init_db(conn: sqlite3.Connection) -> None:
    """Create tables if they don't exist yet."""

    # Creating the schema.
    # Tip: use triple-quoted strings for multi-line SQL.
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS courses (
          id   INTEGER PRIMARY KEY,
          name TEXT NOT NULL,
          term TEXT NOT NULL
        );
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS grades (
          id        INTEGER PRIMARY KEY,
          course_id INTEGER NOT NULL,
          item      TEXT NOT NULL,
          score     REAL NOT NULL CHECK (score >= 0),
          max_score REAL NOT NULL CHECK (max_score > 0),
          FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE
        );
        """
    )
    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_grades_course_id ON grades(course_id);"
    )

    conn.commit()


def prompt_non_empty(label: str) -> str:
    while True:
        value = input(label).strip()
        if value:
            return value
        print("Please enter a value.")


def prompt_int(label: str) -> int:
    while True:
        raw = input(label).strip()
        try:
            return int(raw)
        except ValueError:
            print("Please enter a whole number.")


def prompt_float(label: str) -> float:
    while True:
        raw = input(label).strip()
        try:
            return float(raw)
        except ValueError:
            print("Please enter a number.")


@dataclass(frozen=True)
class Course:
    id: int
    name: str
    term: str

# TODO
def add_course(conn: sqlite3.Connection) -> None:
    name = prompt_non_empty("Course name (ex: CS 1101): ")
    term = prompt_non_empty("Term (ex: Spring 2026): ")

    # (Part A): Insert into courses using a parameterized query.
    # conn.execute(
    #     "INSERT INTO table_name (column1, column2) VALUES (?, ?);",
    #     (value1, value2),
    # )

    conn.commit()

    print("Added course (TODO: wire up INSERT).")

# TODO
def list_courses(conn: sqlite3.Connection) -> list[Course]:
    # (Part B): Query courses and print them.
    # Example query:
    # rows = conn.execute(
    #     "SELECT id, column1, column2 FROM table_name ORDER BY column1;"
    # ).fetchall()

    rows: list[sqlite3.Row] = []

    courses = [Course(id=row["id"], name=row["name"], term=row["term"]) for row in rows]

    if not courses:
        print("No courses yet.")
        return []

    print("\nCourses:")
    for c in courses:
        print(f"  {c.id}. {c.name} ({c.term})")
    print()

    return courses


def select_course_id(conn: sqlite3.Connection) -> int | None:
    courses = list_courses(conn)
    if not courses:
        return None

    course_id = prompt_int("Enter course id: ")
    if course_id not in {c.id for c in courses}:
        print("That course id does not exist.")
        return None

    return course_id

# TODO
def add_grade(conn: sqlite3.Connection) -> None:
    """Add a grade row linked to a course."""

    # (Part C):
    # 1) Choose a course id
    # 2) Prompt for item, score, max_score
    # 3) INSERT into grades (course_id, item, score, max_score)
    # 4) commit

    # HINT: you can reuse and change the add_course() SQL query as a starting point for the INSERT.

    print("TODO: implement add_grade()")

# TODO
def course_report(conn: sqlite3.Connection) -> None:
    """Show all grades for a course + average percent."""

    # (Part D):
    # - Prompt for course id
    # - Query grades + course name (JOIN)
    # - Print each grade
    # - Compute average percent using SUM(score) / SUM(max_score)

    # HINT: example JOIN query:
    # rows = conn.execute(
    #     """
    #     SELECT var1.column1, var1.column2, var1.column3, var2.columnA, var2.columnB
    #     FROM table1 var1
    #     JOIN table2 var2 ON var1.course_id = var2.id
    #     WHERE var2.id = ?;
    #     """,
    #     (var2_id,),
    # ).fetchall()

    print("TODO: implement course_report()")


def print_menu() -> None:
    print("Personal Gradebook")
    print("1) Add course")
    print("2) List courses")
    print("3) Add grade")
    print("4) Course report")
    print("0) Exit")


def main() -> None:
    conn = get_connection(DB_PATH)
    try:
        init_db(conn)

        while True:
            print_menu()
            choice = input("Choose an option: ").strip()

            if choice == "1":
                add_course(conn)
            elif choice == "2":
                list_courses(conn)
            elif choice == "3":
                add_grade(conn)
            elif choice == "4":
                course_report(conn)
            elif choice == "0":
                print("Goodbye.")
                return
            else:
                print("Invalid option.\n")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
