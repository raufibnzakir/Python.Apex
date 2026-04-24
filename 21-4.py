import sqlite3

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    year INTEGER
)
''')

books = [
    ("The Alchemist", "Paulo Coelho", 1988),
    ("Atomic Habits", "James Clear", 2018),
    ("Rich Dad Poor Dad", "Robert Kiyosaki", 1997),
    ("Ikigai", "Héctor García", 2016),
    ("Deep Work", "Cal Newport", 2016)
]


cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
               ("Think and Grow Rich", "Napoleon Hill", 1937))

conn.commit()

cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()

print("Books in database:")
for row in rows:
    print(row)

    conn.close()


