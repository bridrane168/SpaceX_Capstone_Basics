"""Execute SQL analysis against spacex_cleaned_data.csv with SQLite."""
from pathlib import Path
import sqlite3, pandas as pd
BASE = Path(__file__).parent
csv_path = BASE/"data"/"spacex_cleaned_data.csv"
out = BASE/"sql_output"; out.mkdir(exist_ok=True)
conn = sqlite3.connect(":memory:")
pd.read_csv(csv_path).to_sql("spacex",conn,index=False,if_exists="replace")
queries = {
"outcome_counts": "SELECT Class, COUNT(*) AS launches, ROUND(100.0*COUNT(*)/(SELECT COUNT(*) FROM spacex),1) AS pct FROM spacex GROUP BY Class ORDER BY Class",
"launches_by_site": "SELECT LaunchSite, COUNT(*) AS total_launches FROM spacex GROUP BY LaunchSite ORDER BY total_launches DESC",
"success_by_site": "SELECT LaunchSite, COUNT(*) AS total_launches, ROUND(AVG(CAST(Class AS REAL)),3) AS success_rate FROM spacex GROUP BY LaunchSite ORDER BY success_rate DESC",
"payload_by_outcome": "SELECT Class, COUNT(PayloadMass) AS records_with_payload, ROUND(AVG(PayloadMass),2) AS mean_payload_kg, ROUND(MIN(PayloadMass),2) AS min_payload_kg, ROUND(MAX(PayloadMass),2) AS max_payload_kg FROM spacex GROUP BY Class ORDER BY Class"
}
for name, query in queries.items():
    result = pd.read_sql_query(query,conn)
    result.to_csv(out/f"{name}.csv",index=False)
    print(f"\n{name}\n{result.to_string(index=False)}")
conn.close()
