from google.cloud import storage
from params import *

# Initialize the Google Cloud Storage client
client = storage.Client()

# Specify the bucket name and file name you want to work with
preprocessed_data = 'unga_updated.csv'

# Get a reference to the bucket
bucket = client.get_bucket(bucket_name)

# Upload a file to the bucket
blob = bucket.blob(preprocessed_data)
blob.upload_from_filename('path/to/local/file.txt')

# Download a file from the bucket
blob = bucket.blob(file_name)
blob.download_to_filename('path/to/local/downloaded-file.txt')

# List objects in the bucket
blobs = bucket.list_blobs()
for blob in blobs:
    print(f'Object Name: {blob.name}, Size: {blob.size} bytes')

# Delete an object from the bucket
blob = bucket.blob(file_name)
blob.delete()
