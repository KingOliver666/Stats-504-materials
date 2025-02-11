import os
import pandas as pd

# Download the NCDC data, also available from this site:
#  https://www.ncei.noaa.gov/access/search/data-search/daily-summaries

base_url = "https://www.ncei.noaa.gov/data/daily-summaries/access"

target_dir = "C:/Users/16343/Desktop/Stats-504-materials/precip"

files = ["USW00094847.csv", "USW00012839.csv",]

for f in files:
    # Construct the full URL by concatenating base_url, "/", and the file name
    url = f"{base_url}/{f}"

    # Read the CSV directly from the URL
    df = pd.read_csv(url)

    # Create an output filename: "USW00094847.csv.gz", "USW00012839.csv.gz", etc.
    output_path = os.path.join(target_dir, f + ".gz")
    
    # Write out to a gzip-compressed CSV file
    df.to_csv(output_path, index=False, compression='gzip')
