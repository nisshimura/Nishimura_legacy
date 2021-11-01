import json
import boto3
from boto3.dynamodb.conditions import Key
import pprint

def lambda_handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("jobcan")
    for i in range(31):
        response = table.query(
            KeyConditionExpression=Key('No').eq(1000000 + i)
        )
        pprint.pprint(response)
        
    with open(file_path, 'w') as outfile:
    json.dump(data, outfile)
    return response
