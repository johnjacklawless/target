import simplejson as json
import boto3
import sys
import requests
sys.path.insert(0, "vendored")
def geturi(event, context):
  uri_path = event["path"]
  path_dict = uri_path.split('/')
  dynamodb = boto3.resource('dynamodb')
  table = dynamodb.Table('product')
  item = table.get_item(Key={'id': str(path_dict[2])})
  item = item['Item']
  item_price = item['price']
  base_uri = 'https://redsky.target.com/v2/pdp/tcin/'
  item_uri = base_uri + str(path_dict[2])
  r = requests.get(item_uri)
  response = {"statusCode": 200, "body": json.dumps({'Redsky':r.text, 'Price_fromDynamo': item_price})}
  return response

