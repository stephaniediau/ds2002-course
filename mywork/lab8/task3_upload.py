import boto3
import os
import argparse
import logging
import glob

def parse_args():
    parser = argparse.ArgumentParser(description="Upload Lab 07 results to S3")
    parser.add_argument("input_folder", help="Folder with results-*.csv files")
    parser.add_argument("destination", help="Bucket and prefix, e.g., ds2002-ntq7zt/book-analysis/")
    args = parser.parse_args()
    return args.input_folder, args.destination

def upload(input_folder, destination):
    s3 = boto3.client('s3', region_name='us-east-1')
    bucket, *prefix_parts = destination.split("/", 1)
    prefix = prefix_parts[0] if prefix_parts else ""
    files = glob.glob(os.path.join(input_folder, "results-*.csv"))
    if not files:
        logging.warning(f"No results-*.csv files found in {input_folder}")
        return
    for file_path in files:
        key = os.path.join(prefix, os.path.basename(file_path))
        try:
            with open(file_path, 'rb') as f:
                s3.put_object(Bucket=bucket, Key=key, Body=f)
            logging.info(f"Uploaded {file_path} to s3://{bucket}/{key}")
        except Exception as e:
            logging.error(f"Failed to upload {file_path}: {e}")

def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    input_folder, destination = parse_args()
    upload(input_folder, destination)
    logging.info("Upload process complete.")

if __name__ == "__main__":
    main()
