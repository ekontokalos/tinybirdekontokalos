import os
import requests
import pandas as pd
import pyarrow.parquet as pq
from io import BytesIO

# Switch these values to the desired date range
start_date=2009
end_date=2024

#Months that have not been added to the site will say "Failed to download"
# Function to download the data for a given year and month
def download_taxi_data(year, month):
    url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year}-{month:02d}.parquet"
    print(f"Downloading {url}")
    response = requests.get(url)
    
    if response.status_code == 200:
        return pd.read_parquet(BytesIO(response.content))
    else:
        print(f"Failed to download {url}")
        return None

# Function to loop through years and months, download data and combine into a DataFrame
def download_all_taxi_data(start_year, end_year):
    all_data = []
    
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            df = download_taxi_data(year, month)
            if df is not None:
                all_data.append(df)
    
    if all_data:
        return pd.concat(all_data, ignore_index=True)
    else:
        return pd.DataFrame()  
df = download_all_taxi_data(start_date, end_date)

def filter_by_percentile(df, column_name, percentile):
    """
    Parameters:
    df: The input DataFrame.
    column_name (str): The name of the column to calculate the percentile for.
    percentile (float): The percentile to filter by (e.g., 0.9 for the 90th percentile).

    Returns:
    The filtered DataFrame.
    """
    threshold = df[column_name].quantile(percentile)
    filtered_df = df[df[column_name] > threshold]
    return filtered_df

# You can change the percentile of trip_distance by stating it in the function below
filtered_df = filter_by_percentile(df, 'trip_distance', 0.9)
file_name = f"yellow_taxi_data_filtered_{start_date}_{end_date}.parquet"
# Call the function
filtered_df.to_parquet(file_name, engine='pyarrow')
print(f"Data saved to {file_name}")
