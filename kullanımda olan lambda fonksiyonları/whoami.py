import os
import json
        
def lambda_handler(event, context):


    fullname = {
    "firstname": event['queryStringParameters']['firstname'],
    "lastname": event['queryStringParameters']['lastname']
    }
    

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(fullname)
        
    }