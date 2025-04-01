import boto3

class ThingDAO:
    def __init__(self):
        dynamodb = boto3.resource('dynamodb')
        self.table = dynamodb.Table('things')

    def get_thing(self, thing_id):
        response = self.table.get_item(Key={'id': thing_id})
        return response.get('Item')