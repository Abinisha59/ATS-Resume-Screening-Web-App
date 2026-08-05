import sqlite3

conn = sqlite3.connect("resume.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS resume_history (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    filename TEXT,

    role TEXT,

    score INTEGER,

    matched TEXT,

    missing TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

conn.commit()

conn.close()

print("Database and table created successfully.")