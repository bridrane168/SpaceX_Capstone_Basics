"""Scrape historical Falcon 9 launch tables. Run with: python scrape_launches.py"""
from pathlib import Path
import pandas as pd
OUT = Path(__file__).parent / "scraping_output"; OUT.mkdir(exist_ok=True)
url = "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches"
tables = pd.read_html(url)
print("Tables found:",len(tables))
for i, table in enumerate(tables):
    print(f"\nTABLE {i}: shape={table.shape}; columns={list(table.columns)}")
    print(table.head(3).to_string(index=False))
# Preserve all candidate tables; inspect and select the appropriate historical launch table.
with pd.ExcelWriter(OUT/"launch_tables.xlsx") as writer:
    for i, table in enumerate(tables):
        table.to_excel(writer,sheet_name=f"table_{i}"[:31],index=False)
print("Saved candidate tables to",OUT/"launch_tables.xlsx")
