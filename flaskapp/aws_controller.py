import boto3 as boto3

dynamo_client = boto3.client('dynamodb', "us-east-1")
TABLE_NAME='Pokemon'


def get_items():
    return dynamo_client.scan(
        TableName='Pokemon'
    )

def post_items(name, type):
    dynamo_client.put_item(TableName=TABLE_NAME, Item={'name': {'S': name}, 'type': {'S': type}})
    return "Successfully added " + name + " to the database"