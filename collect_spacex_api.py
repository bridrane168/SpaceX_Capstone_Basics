"""Fetch current launch records from SpaceX API v4. Run with: python collect_spacex_api.py"""
from pathlib import Path
import json, requests, pandas as pd
OUT = Path(__file__).parent / "api_output"; OUT.mkdir(exist_ok=True)
url = "https://api.spacexdata.com/v4/launches/query"
payload = {"query": {}, "options": {"pagination": False, "sort": {"date_utc": "asc"}}}
r = requests.post(url, json=payload, timeout=60)
r.raise_for_status()
raw = r.json()
(OUT/"launches_raw.json").write_text(json.dumps(raw,indent=2),encoding="utf-8")
docs = raw.get("docs", []) if isinstance(raw,dict) else raw
rows = []
for x in docs:
    rows.append({"flight_number":x.get("flight_number"),"name":x.get("name"),"date_utc":x.get("date_utc"),
                 "success":x.get("success"),"launchpad":x.get("launchpad"),"payloads":x.get("payloads"),
                 "rocket":x.get("rocket"),"upcoming":x.get("upcoming")})
pd.DataFrame(rows).to_csv(OUT/"launches_api.csv",index=False)
print("HTTP status:",r.status_code,"records:",len(rows))
print(pd.DataFrame(rows).head().to_string(index=False))
