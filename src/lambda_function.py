import json
from thing_service import ThingService
from thing_dao import ThingDAO

thing_service = ThingService(ThingDAO())

def lambda_handler(event, context):
    thing_id = event['pathParameters']['id']

    try:
        item = thing_service.get_thing(thing_id)

        if not item:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Thing not found'})
            }

        return {
            'statusCode': 200,
            'body': json.dumps(item)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }