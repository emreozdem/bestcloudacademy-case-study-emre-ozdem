import json


def lambda_handler(event,context):
    firstname=event['queryStringParameters']['firstname']
    lastname=event['queryStringParameters']['lastname']
  

    print('firstname='+ firstname)
    print('lastname='+ lastname)


    #Feedback objesi

    transactionResponse={}
    transactionResponse['firstname']=firstname
    transactionResponse['lastname']=lastname
    transactionResponse['message']='Seeaa'

    #HTTP feedback obj

    responseObject= {}
    responseObject['statusCode']=200
    responseObject['headers']
    responseObject['headers'][Content-Type]='application/json'
    responseObject['body']=json.dumps(transactionResponse)

    #Response

    return responseObject

    


    