import os
import json
        
def lambda_handler(event, context):

    

    fullname = {
    "firstname": event['queryStringParameters']['firstname'],
    "lastname": event['queryStringParameters']['lastname']
    }

    if event['queryStringParameters']['firstname'] is None:
        event['queryStringParameters']['firstname']="null"

    if event['queryStringParameters']['lastname'] is None:
        event['queryStringParameters']['lastname']="null"
 
    
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(fullname)
        
    }