#!/usr/bin/env python3

import requests
import pandas as pd
import sys
import logging
import os
import mysql.connector

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[console_handler])

URL = "http://api.open-notify.org/iss-now.json"

def connect_db():
    return mysql.connector.connect(
        host=os.getenv("DBHOST"),
        user=os.getenv("DBUSER"),
        password=os.getenv("DBPASS"),
        database="iss"
    )

def extract(url):
    """
    Extracts data from the ISS API and returns it as a JSON object.
    """
    logging.info(f"Getting data from URL: {url}")
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
    logging.info(f"Transforming 1 row of data")

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

def register_reporter(table, reporter_id, reporter_name):

    db = connect_db()
    cursor = db.cursor()

    query = f"SELECT * FROM {table} WHERE reporter_id = %s"
    cursor.execute(query, (reporter_id,))
    result = cursor.fetchone()

    if result is None:
        insert = f"INSERT INTO {table} (reporter_id, reporter_name) VALUES (%s, %s)"
        cursor.execute(insert, (reporter_id, reporter_name))
        db.commit()
        logging.info("Reporter registered")
    else:
        logging.info("Reporter already exists")

    cursor.close()
    db.close()

def load(df, reporter_id):

    db = connect_db()
    cursor = db.cursor()

    row = df.iloc[0]

    message = "success"
    latitude = row["latitude"]
    longitude = row["longitude"]
    timestamp = row["timestamp"]

    query = """
        INSERT INTO locations (message, latitude, longitude, timestamp, reporter_id)
        VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(query, (message, latitude, longitude, timestamp, reporter_id))
    db.commit()

    logging.info("Loaded ISS location into database")

    cursor.close()
    db.close()

def main():
    """
    Main function for the ETL process for ISS data.
    """
    logging.info("Starting ETL process for ISS data")

    reporter_id = "ntq7zt"
    reporter_name = "Stephanie Diau"

    register_reporter("reporters", reporter_id, reporter_name)

    data = extract(URL)
    df = transform(data)
    load(df, reporter_id)

    logging.info("ETL process completed successfully!")

if __name__ == "__main__":
    main()