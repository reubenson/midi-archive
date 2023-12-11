#!/bin/bash

DIRECTORY="../tokens_noBPE"
BUCKET="midi-archive"
BUCKET_DIR="assets/tokens"
TOKENS_ZIP_PATH="../tokens.zip"

# Upload the directory to the S3 bucket
# aws s3 cp --recursive $DIRECTORY s3://$BUCKET/$BUCKET_DIR/ --acl public-read

# Zip and upload the entire tokens directory (generated with apply_tokenizer.py)
zip -r $TOKENS_ZIP_PATH $DIRECTORY
aws s3 cp $TOKENS_ZIP_PATH s3://$BUCKET/$BUCKET_DIR/ --acl public-read

# Upload tokenizer config (generated with apply_tokenizer.py)
TOKENS_CONFIG_PATH=$DIRECTORY/_tokenizer.json
aws s3 cp $TOKENS_CONFIG_PATH s3://$BUCKET/$BUCKET_DIR/ --acl public-read