import sqlite3
import os

def get_db_connection():
    db_path = os.path.join(os.path.dirname(__file__), '..', 'database', 'crime_tracking.db')
    db_path = os.path.abspath(db_path)  # Important: Full path
    conn = sqlite3.connect(db_path)
    return conn

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS crime_reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            date TEXT,
            location TEXT
        )
    ''')
    conn.commit()
    conn.close()


