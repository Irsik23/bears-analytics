import pandas as pd
import sqlite3

# 1. SETUP
target_year = 2025
target_team = 'CHI'
url = f"https://github.com/nflverse/nflverse-data/releases/download/pbp/play_by_play_{target_year}.parquet"

print(f"--- STARTING DIRECT DOWNLOAD FOR {target_year} ---")

# 2. DOWNLOAD
print(f"Pulling data from: {url}")
df = pd.read_parquet(url)

# 3. FILTERING
print("Filtering for Bears...")
bears_offense = df[
    (df['posteam'] == target_team) & 
    (df['play_type'].isin(['run', 'pass'])) &
    (df['play_type'].notna())
]

# 4. CLEANING (Now with GAME_ID!)
clean_data = pd.DataFrame()
clean_data['game_id'] = bears_offense['game_id']
clean_data['quarter'] = bears_offense['qtr']
clean_data['time_remaining'] = bears_offense['quarter_seconds_remaining']
clean_data['team'] = bears_offense['posteam']
clean_data['opponent'] = bears_offense['defteam']
clean_data['down'] = bears_offense['down']
clean_data['togo'] = bears_offense['ydstogo']
clean_data['yards_gained'] = bears_offense['yards_gained']
clean_data['play_type'] = bears_offense['play_type']

clean_data = clean_data.fillna(0)

print(f"Found {len(clean_data)} offensive plays.")

# 5. INGESTION (The Fix: 'replace' rebuilds the table)
print("Rebuilding database...")
conn = sqlite3.connect('bears_stats.db')
clean_data.to_sql('plays', conn, if_exists='replace', index=False)
conn.close()

print("[SUCCESS] Database updated with Game IDs.")
