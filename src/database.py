# database.py
import sqlite3

DB_NAME = "books.db"


def init_db(df):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            genre TEXT
        )
    """)

    cursor.execute("DELETE FROM books")

    for _, row in df.iterrows():
        cursor.execute(
            "INSERT INTO books (title, author, genre) VALUES (?, ?, ?)",
            (row["title"], row["author"], row["genre"])
        )

    conn.commit()
    conn.close()


def get_books():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT title FROM books")

    books = cursor.fetchall()

    conn.close()

    return [b[0] for b in books]