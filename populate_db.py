import sqlite3

# 1. THE RAW DATA (The Feed)
# This mimics what you get from an API.
# Format: (Quarter, Time, Team, Opponent, Down, ToGo, Yards, Type)
scouting_data = [
    (1, "14:55", "CHI", "GB", 1, 10, 4, "run"),
    (1, "14:20", "CHI", "GB", 2, 6, 8, "pass"),
    (1, "13:45", "CHI", "GB", 1, 10, 45, "pass"), # EXPLOSIVE
    (1, "13:10", "CHI", "GB", 1, 10, -2, "run"),
    (1, "12:30", "CHI", "GB", 2, 12, 12, "run"),  # EXPLOSIVE
    (2, "08:15", "GB", "CHI", 1, 10, 0, "pass"),
    (2, "07:50", "GB", "CHI", 2, 10, 65, "pass"), # EXPLOSIVE (Against us)
    (3, "11:00", "CHI", "MIN", 1, 10, 3, "run"),
    (3, "10:25", "CHI", "MIN", 2, 7, 22, "pass"), # EXPLOSIVE
    (4, "01:55", "CHI", "DET", 1, 10, 0, "run"),
    (4, "01:50", "CHI", "DET", 2, 10, 15, "pass"),
]

# 2. CONNECT TO THE VAULT
conn = sqlite3.connect('bears_stats.db')
cursor = conn.cursor()

# 3. THE INGESTION (Batch Insert)
# "executemany" is a senior-level trick. It's 100x faster than a loop.
cursor.executemany('''
    INSERT INTO plays (quarter, time_remaining, team, opponent, down, togo, yards_gained, play_type)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''', scouting_data)

# 4. COMMIT AND CLOSE
conn.commit()
conn.close()

print(f"[SUCCESS] Ingested {len(scouting_data)} plays into the database.")
