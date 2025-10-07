import boto3
import sys

s3 = boto3.client(
    's3',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test'
)

bucket_name = 'mediastorage'

def upload_file(file_path):
    file_name = file_path.split('/')[-1]
    s3.upload_file(file_path, bucket_name, file_name)
    print(f"Uploaded {file_name} to bucket {bucket_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python upload_to_s3.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    upload_file(file_path)
    sys.exit(0)