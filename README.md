Here’s a more concise version of the `README.md`:

---

# NYC Yellow Taxi Trips: 90th Percentile Distance Filter

## Task
Identify all NYC Yellow Taxi trips above the 0.9 percentile in distance traveled using parquet files from 2020-2024.

## Solution
1. **Data Download**: A script downloads monthly trip data for the specified range (2020-2024) and combines it into a single parquet file.
2. **Percentile Calculation**: The combined dataset is filtered to extract trips exceeding the 90th percentile in `trip_distance`.

## Reproduce Steps
1. **Clone Repo**:
   ```bash
   git clone git@github.com:ekontokalos/tinybirdekontokalos.git
   cd tinybirdekontokalos
   ```
2. **Install Dependencies**:
   ```bash
   pip install pandas pyarrow requests
   ```
3. **Run Data Download**:
   ```bash
   python data_download.py
   ```
4. **Filter by Percentile**:
   ```bash
   python data_explore.py
   ```

Data is saved to a dynamic parquet file based on the date range.
