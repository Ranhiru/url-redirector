import json
import secrets
import boto3
import os
from datetime import datetime

def create_redirection(event, context):
    body = json.loads(event["body"])
    url = body["url"]

    key = save_url(url)
    response = {'key': key}

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }

def save_url(url):
    key = get_unique_token(os.getenv("TOKEN_SIZE", 10))
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.getenv('TABLE_NAME'))
    table.put_item(
       Item={
            'id': key,
            'url': url,
            'created_at_utc': str(datetime.utcnow())
        }
    )
    return key

def get_unique_token(token_size):
  return secrets.token_urlsafe(int(token_size))
