# SpaceX Falcon 9 First-Stage Landing Prediction

This repository bundle contains the revised notebook, analysis outputs, SQL results, model evaluation, map, and scripts for the IBM Applied Data Science Capstone.

## Dataset
- File: `data/spacex_cleaned_data.csv`
- 90 launch records
- Target: `Class` (0 = unsuccessful, 1 = successful)
- Observed outcome balance: 30 unsuccessful and 60 successful launches

## Included and executed
- `SpaceX_Capstone_Basics_executed.ipynb`: executed copy of the starter notebook with outputs embedded (loads the local CSV).
- `data/data_quality_report.csv`: data types and missingness by column.
- `sql_output/`: four executed SQLite query outputs and their SQL statements.
- `data/fresh_model_metrics.csv` and `logs/model_evaluation.txt`: fresh model metrics and confusion matrices computed from held-out predictions.
- `figures/`: outcome distribution, site success, payload comparison, flight-group trend, and confusion-matrix charts.
- `web/spacex_launch_sites.html`: interactive Folium map with site markers and popups.
- `web/spacex_dash_app.py`: interactive Plotly Dash dashboard source.
- `web/collect_spacex_api.py` and `web/scrape_launches.py`: scripts for API collection and web-table scraping.

## Important evidence status
The analysis, SQLite queries, model evaluation, charts, and Folium HTML were generated from the uploaded cleaned CSV in this run. The API collection and web-scraping scripts are provided but their live network outputs are not included; run them with internet access before claiming those steps are completed. The Dash source is provided but must be run locally to capture authentic screenshots.

## Run locally
1. Install Python 3.10+.
2. Install dependencies: `pip install -r requirements.txt`
3. Run SQL script from this folder: `python web/sql_analysis.py` (expects the CSV under `data/`).
4. Run dashboard: `python web/spacex_dash_app.py`, then open `http://127.0.0.1:8050`.
5. Run API script: `python web/collect_spacex_api.py`.
6. Run scraper: `python web/scrape_launches.py`.
7. Open `web/spacex_launch_sites.html` in a browser to inspect the interactive map.

## Model results
Fresh stratified 75/25 train/test split with `random_state=42`:
- Decision Tree: accuracy 86.96%, precision 87.50%, recall 93.33%, F1 90.32%.
- Logistic Regression: accuracy 82.61%, precision 78.95%, recall 100.00%, F1 88.24%.

These are small-sample retrospective baseline results. Check whether every predictor would be available at the intended prediction time, and avoid interpreting these scores as operational guarantees.
