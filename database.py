import sqlite3

conn = sqlite3.connect("finance.db", check_same_thread=False)
cursor = conn.cursor()

def create_tables():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    """)
    conn.commit()

def set_setting(key, value):
    cursor.execute(
        "INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)",
        (key, value)
    )
    conn.commit()

def get_setting(key):
    cursor.execute(
        "SELECT value FROM settings WHERE key = ?",
        (key,)
    )
    row = cursor.fetchone()
    return row[0] if row else None
