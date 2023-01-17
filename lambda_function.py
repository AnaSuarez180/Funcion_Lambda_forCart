import json
import os
import mercadopago


def lambda_handler(event, context):
    sdk = mercadopago.SDK(os.environ["VITE_ACCESS_TOKEN"])
    

    bodyGet = event
    items = [{
        "id": "item1",
        "title": "item1 title",
        "quantity": 1,
        "unit_price": 50
    }]

    # TODO implement
    preference_data = {
        "items": items
        
    }



    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]

    return {
        "statusCode": 200,
        "headers": {
            'Access-Control-Allow-Headers': 'Content-Type,X-Amz-Date,X-Amz-Security-Token,Authorization,X-Api-Key,X-Requested-With,Accept,Access-Control-Allow-Methods,Access-Control-Allow-Origin,Access-Control-Allow-Headers',
            'Access-Control-Allow-Origin': "*",
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        "body": json.dumps(
            preference
        ),
    }