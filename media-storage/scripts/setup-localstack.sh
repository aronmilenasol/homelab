#!/usr/bin/env bash

set -euo pipefail

mkdir -p volume

export AWS_ACCESS_KEY_ID="test"
export AWS_SECRET_ACCESS_KEY="test"
export AWS_DEFAULT_REGION="us-east-1"

if ! command -v aws &> /dev/null
then
    echo "AWS CLI could not be found, please install it"
    exit 1
fi 

if ! command -v docker &> /dev/null
then
    echo "Docker could not be found, please install it"
    exit 1
fi

echo "Starting LocalStack..."