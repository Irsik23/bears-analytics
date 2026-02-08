import sqlite3

# 1. CONNECT
# This creates the file 'bears_stats.db' if it doesn't exist.
conn = sqlite3.connect('bears_stats.db')
cursor = conn.cursor()

# 2. THE SCHEMA (The Blueprint)
# We are designing a table called "plays" to hold our scouting data.
# REAL WORLD NOTE: "IF NOT EXISTS" prevents crashing if you run this twice.
cursor.execute('''
    CREATE TABLE IF NOT EXISTS plays (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        quarter INTEGER,
        time_remaining TEXT,
        team TEXT,
        opponent TEXT,
        down INTEGER,
        togo INTEGER,
        yards_gained INTEGER,
        play_type TEXT
    )
''')

# 3. SAVE AND CLOSE
conn.commit()
conn.close()

print("[SUCCESS] Database 'bears_stats.db' created with table 'plays'.")
