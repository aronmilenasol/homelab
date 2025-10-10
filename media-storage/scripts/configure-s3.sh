#!/usr/bin/env bash
set -euo pipefail

echo "Setting up S3 bucket in LocalStack..."

BUCKET_NAME="mediastorage"
URL="http://localhost:4566"

aws --endpoint-url=$URL s3 mb s3://$BUCKET_NAME

aws --endpoint-url=$URL s3api put-bucket-cors \
    --bucket $BUCKET_NAME \
    --cors-configuration file://media-storage/cors-config.json

aws --endpoint-url=$URL s3 cp testing/files-to-upload/test.txt s3://$BUCKET_NAME/

echo "Bucket $BUCKET_NAME created, configured, and tested."
