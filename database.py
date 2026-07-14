import sqlite3

DB = "automation.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        command TEXT,
        result TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS scheduled_tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        command TEXT,
        schedule TEXT
    )
    """)

    conn.commit()
    conn.close()


def log_history(command, result):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("INSERT INTO history (command, result) VALUES (?, ?)", (command, result))
    conn.commit()
    conn.close()


def get_history():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT command, result FROM history ORDER BY id DESC LIMIT 20")
    rows = c.fetchall()
    conn.close()
    return rows