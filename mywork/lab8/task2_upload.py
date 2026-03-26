import boto3
import os

BUCKET = 'ds2002-ntq7zt'
PRIVATE_FILE = '/home/ntq7zt/ds2002-course/sleepy.jpg'
PUBLIC_FILE = '/home/ntq7zt/ds2002-course/bed.jpg'

s3 = boto3.client('s3', region_name='us-east-1')

private_key = os.path.basename(PRIVATE_FILE)
public_key = os.path.basename(PUBLIC_FILE)

with open(PRIVATE_FILE, 'rb') as f:
    s3.put_object(Bucket=BUCKET, Key=private_key, Body=f)

presigned_url = s3.generate_presigned_url(
    'get_object', Params={'Bucket': BUCKET, 'Key': private_key}, ExpiresIn=3600
)
print(f"Private file uploaded. Presigned URL: {presigned_url}")

with open(PUBLIC_FILE, 'rb') as f:
    s3.put_object(Bucket=BUCKET, Key=public_key, Body=f, ACL='public-read')

print(f"Public file uploaded: https://s3.amazonaws.com/{BUCKET}/{public_key}")