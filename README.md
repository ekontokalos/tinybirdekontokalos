Here’s the corrected `README.md` reflecting the 2009-2024 date range:

---

# NYC Yellow Taxi Trips: 90th Percentile Distance Filter

## Task
Identify NYC Yellow Taxi trips above the 0.9 percentile in distance traveled 
## Solution

### Approach
1. **Data Download**:
   I leveraged the URL's year and month parameters to automate data downloads via a loop, covering the range from 2009-2024. Missing months are handled simply with a "Failed to download" message and they continue without interruption.

2. **Dynamic File Naming**:
   The output file name is dynamically based on the date range (`start_year` and `end_year`), making it easy to organize and identify files corresponding to specific time periods.

3. **Percentile Filtering**:
   The script filters trips above the 90th percentile for `trip_distance`, ensuring that only the longest trips are included. The results are saved to a parquet file named according to the date range.

### Key Points
- Automated download for the full date range.
- Dynamic file naming for clarity and organization.
- Focuses on the longest trips based on `trip_distance`.

## Reproduction Steps
1. **Clone Repo**:
   ```bash
   git clone git@github.com:ekontokalos/tinybirdekontokalos.git
   cd tinybirdekontokalos
   ```
2. **Install Dependencies**:
   ```bash
   pip install pandas pyarrow requests
   ```
3. **Run Data Download and Filtering**:
   ```bash
   python download_filter_taxi.py
   ```
