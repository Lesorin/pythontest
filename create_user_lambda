import json
import uuid
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

def lambda_handler(event, context):
    body = json.loads(event['body'])

    user_id = str(uuid.uuid4())
    first_name = body.get('first_name')
    age = body.get('age')

    if not first_name or not isinstance(age, int):
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid input"})
        }

    item = {
        'user_id': user_id,
        'first_name': first_name,
        'age': age
    }

    table.put_item(Item=item)

    return {
        "statusCode": 200,
        "body": json.dumps({"user_id": user_id})
    }
