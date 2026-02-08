import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. SETUP & STYLE
plt.switch_backend('Agg')
# Use a clean, grid-based theme
sns.set_theme(style="whitegrid", context="talk")

# 2. DATA INGESTION
conn = sqlite3.connect('bears_stats.db')
df = pd.read_sql("SELECT * FROM plays", conn)
conn.close()

# 3. LOGIC (The "Explosive" Filters)
explosive_runs = (df['play_type'] == 'run') & (df['yards_gained'] >= 10)
explosive_pass = (df['play_type'] == 'pass') & (df['yards_gained'] >= 20)
df['is_explosive'] = explosive_runs | explosive_pass

# Filter down to just the explosive plays
chart_data = df[df['is_explosive'] == True]

# Count them up so we can plot exact numbers
summary = chart_data['play_type'].value_counts().reset_index()
summary.columns = ['play_type', 'count']

# 4. THE PRO VISUALIZATION
plt.figure(figsize=(10, 8))

# OFFICIAL BEARS HEX CODES
# Navy: #0B162A | Orange: #C83803
bears_palette = {'run': '#0B162A', 'pass': '#C83803'}

# Draw the bars
ax = sns.barplot(
    data=summary, 
    x='play_type', 
    y='count', 
    palette=bears_palette,
    order=['pass', 'run'] # Put Pass first (usually the bigger number)
)

# 5. ANNOTATIONS (The "ESPN" Look)
# Add the specific numbers on top of the bars
for container in ax.containers:
    ax.bar_label(container, fontsize=18, weight='bold', padding=5)

# Clean up the chart junk
sns.despine(left=True, bottom=True)
ax.set_ylabel('')
ax.set_xlabel('')
ax.set_yticklabels([]) # Hide the left-side numbers (since we have labels on bars)
ax.grid(False) # Clean look

# 6. TITLES & BRANDING
plt.title("2025 CHICAGO BEARS\nEXPLOSIVE PLAY BREAKDOWN", 
          fontsize=22, weight='bold', loc='center', color='#0B162A')

plt.figtext(0.5, 0.88, "Criteria: Run > 10 yds | Pass > 20 yds", 
            ha="center", fontsize=12, color='gray')

plt.figtext(0.5, 0.05, "Source: Bears Analytics Suite (nflverse data)", 
            ha="center", fontsize=10, color='gray')

# 7. SAVE HIGH-RES ASSET
plt.savefig('bears_pro_chart.png', dpi=300, bbox_inches='tight')
print("[SUCCESS] Professional chart generated: 'bears_pro_chart.png'")
