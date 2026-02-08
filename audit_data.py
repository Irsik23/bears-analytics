import sqlite3
import pandas as pd

# 1. CONNECT
conn = sqlite3.connect('bears_stats.db')

# 2. CHECK GAME COUNT (Should be 17 for a full season)
print("--- DATA INTEGRITY CHECK ---")
game_query = "SELECT COUNT(DISTINCT game_id) as games_played FROM plays"
games = pd.read_sql(game_query, conn)
print(f"Games in Database: {games['games_played'][0]} (Should be 17)")

# 3. CHECK CALEB WILLIAMS PASSING YARDS
# Official 2025 Stat: ~3,942 Yards
yards_query = """
    SELECT 
        SUM(yards_gained) as total_yards
    FROM plays
    WHERE play_type = 'pass' 
    AND team = 'CHI'
"""
yards = pd.read_sql(yards_query, conn)
print(f"Total Passing Yards: {yards['total_yards'][0]} (Official: ~3,942)")

conn.close()
