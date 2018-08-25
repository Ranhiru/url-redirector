import secrets

def create_redirection(event, context):
    return {
      "statusCode": 200,
      "body": { "key": "XXXX-YYYY-ZZZZZ" }
    }

def get_unique_token(token_size):
  return secrets.token_urlsafe(token_size)