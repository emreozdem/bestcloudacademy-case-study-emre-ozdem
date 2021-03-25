import json

print('Loading Function')
def lambda_handler(event,context):
    transactionId=event['queryStringParameters']['transactionId']
    transactionType=event['queryStringParameters']['type']
    transactionAmount=event['queryStringParameters']['amount']

    print('transactionId='+ transactionId)
    print('transactionType='+ transactionType)
    print('transactionAmount='+ transactionAmount)

    #Feedback objesi

    transactionResponse={}
    transactionResponse['transactionId']=transactionId
    transactionResponse['type']=transactionType
    transactionResponse['amount']=transactionAmount
    transactionResponse['message']='Seeaa'

    #HTTP feedback obj

    responseObject= {}
    responseObject['statusCode']=200
    responseObject['headers']
    responseObject['headers'][Content-Type]='application/json'
    responseObject['body']=json.dumps(transactionResponse)

    #Response

    return responseObject

    


    