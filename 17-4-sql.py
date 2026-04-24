# import sqlite3

# conn = sqlite3.connect('employees.db')
# cursor = conn.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
#     id INTEGER PRIMARY KEY,
#     name TEXT,
#     age INTEGER
# )''')

# names = ['pratik', 'himesh', 'vinay', 'pritesh', 'rauf']
# ages = [23, 21, 22, 25, 21]

# for name, age in zip(names, ages):
#     cursor.execute("INSERT INTO employees (name, age) VALUES (?, ?)", (name, age))

# conn.commit()

# cursor.execute("SELECT * FROM employees")
# print("Before delete:", cursor.fetchall())

# cursor.execute("DELETE FROM employees WHERE name = ?", ("pratik",))
# conn.commit()

# cursor.execute("SELECT * FROM employees")
# print("After delete:", cursor.fetchall())


# cursor.execute("INSERT INTO employees (name, age) VALUES (?, ?)", ("Alex", 24))

# conn.commit()
# cursor.execute("SELECT * FROM employees")
# print("After inserting Alex:", cursor.fetchall())

# conn.close()

