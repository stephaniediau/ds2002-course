#!/usr/bin/env python3

import requests
import json
import pandas as pd
import sys
import logging
import os

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[console_handler])

URL = "http://api.open-notify.org/iss-now.json"


def parse_args():
    try:
        csv_file = sys.argv[1]
    except IndexError:
        logging.error(f"Usage: python {sys.argv[0]} <csv_file>")
        sys.exit(1)
    return csv_file

def extract(url):
    """
    Extracts data from the ISS API and returns it as a JSON object.
    """
    logging.info(f"Getting data from URl")
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logging.info("Extracted ISS data successfully")
        return data
    except requests.exceptions.RequestException as e:
        logging.error(f"Request error: {e}")
        sys.exit(1)

def transform(data):
    """
    Transforms the extracted data into a pandas DataFrame with timestamp.
    """
    logging.info(f"Transforming data")

    timestamp = pd.to_datetime(data["timestamp"], unit="s")
    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])

    df = pd.DataFrame([{
        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "latitude": latitude,
        "longitude": longitude
    }])
    logging.info(f"Transformed: {df.shape[0]} row × {df.shape[1]} columns")
    return df


def load(df, csv_file):
    """
    Loads the DataFrame into a CSV file, appending to our specified CSV file. 
    """
    if os.path.exists(csv_file):
        df.to_csv(csv_file, mode='a', header=False, index=False)
    else:
        df.to_csv(csv_file, mode='w', header=True, index=False)

    logging.info(f"Loaded data into {csv_file}")

def main():
    """
    Main function for the ETL process for ISS data.
    """
    logging.info(f"Starting ETL process for ISS data")
    csv_file = parse_args()
    data = extract(URL)
    df = transform(data)
    load(df, csv_file)

    logging.info(f"Processed {len(df)} record")

if __name__ == "__main__":
    main()