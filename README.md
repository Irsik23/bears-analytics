# Chicago Bears 2025 Offensive Analytics Suite

## 🏈 Project Overview
An automated data pipeline designed to analyze the Chicago Bears' offensive efficiency during the 2025-2026 season. This tool ingests raw NFL play-by-play data, filters for "Explosive Plays" (Run > 10yds, Pass > 20yds), and generates scouting reports for coaching staff.

**Key Result:** Identified and visualized 152 explosive plays (86 Pass / 66 Run) across the 19-game season (Regular Season + Playoffs).

## 🛠 Tech Stack
* **Language:** Python 3.12
* **Data Processing:** Pandas (ETL), NumPy
* **Database:** SQLite (Relational Storage)
* **Visualization:** Matplotlib, Seaborn
* **Source:** nflverse (Parquet ingestion)

## 🚀 Engineering Features
* **Direct Ingestion Engine:** Bypassed unstable API wrappers to ingest raw Parquet files directly from source.
* **Data Integrity Protocol:** Implemented `audit_data.py` to verify database stats against official NFL records (validated 99.8% accuracy on Passing Yards).
* **"Penalty Trap" Cleaning:** Custom logic to reclaim explosive plays negated by defensive penalties, which are often discarded by standard scrapers.
* **Automated Reporting:** One-click generation of `bears_pro_chart.png` for weekly efficiency reviews.

## 📊 Sample Output
*(See `bears_pro_chart.png` in file list)*
* **Navy Bar:** Run Explosives (66)
* **Orange Bar:** Pass Explosives (86)

## 💻 How to Run
1.  **Install Dependencies:**
    ```bash
    pip install pandas matplotlib seaborn pyarrow
    ```
2.  **Run the Pipeline:**
    ```bash
    python3 scrape_real_data.py  # Ingests fresh 2025 data
    python3 explosive_report.py  # Generates the visualization
    ```

---
*Built by Bailey*
