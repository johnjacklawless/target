import simplejson as json
import boto3
import sys
sys.path.insert(0, "vendored")
def geturi(event, context):
  uri_path = event["path"]
  path_dict = uri_path.split('/')
  dynamodb = boto3.resource('dynamodb')
  table = dynamodb.Table('product')
  item = table.get_item(Key={'id': str(path_dict[2])})
  body = {}
  response = {"statusCode": 200, "body": json.dumps(item['Item'])}
  return response