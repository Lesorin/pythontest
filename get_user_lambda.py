import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

def lambda_handler(event, context):
    user_id = event['pathParameters']['user_id']

    response = table.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key('user_id').eq(user_id)
    )

    items = response.get('Items')
    if not items:
        return {
            "statusCode": 404,
            "body": json.dumps({"error": "User not found"})
        }

    return {
        "statusCode": 200,
        "body": json.dumps(items[0])
    }
