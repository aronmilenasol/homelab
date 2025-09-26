import boto3
import os
from datetime import datetime
import shutil
import tarfile

s3 = boto3.client(
    's3',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test'
)

bucket_name = 'mediastorage'
backup_name = 'mediastorage_backup'
backup_dir = '../backups'
tmp_dir = '../tmp'

os.makedirs(backup_dir, exist_ok=True)
os.makedirs(tmp_dir, exist_ok=True)

timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
backup_file_path = os.path.join(backup_dir, f"{backup_name}_{timestamp}.tar.gz")

objects = s3.list_objects_v2(Bucket=bucket_name)
for obj in objects.get('Contents', []):
    key = obj['Key']
    local_file = os.path.join(tmp_dir, key)
    s3.download_file(bucket_name, key, local_file)
    print(f"Downloaded {key} to {local_file}")

with tarfile.open(backup_file_path, "w:gz") as tar:
    tar.add(tmp_dir, arcname=os.path.basename(tmp_dir))

print(f"Backup completed: {backup_file_path}")

shutil.rmtree(tmp_dir)