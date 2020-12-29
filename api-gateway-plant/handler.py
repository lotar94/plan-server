import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

def hello(event, context):
    name = event['pathParameters']['name']
    body = {
        "message": name + " WENA WENA SERVERLES ES LA CUMBIA",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response

def addMeasurement(event, context):
    try:
        print("------------event------------")
        print(event)
        print("------------event------------")
        #Conexion con la DB y seleccion de la tabla para insertar los datos
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('measurementTable')

        #Se obtiene el body desde el event de la funcion lambda
        jsonPerson = json.loads(event['body'])
        print("-------------El body-------------")
        print(jsonPerson)
        print("-------------El body-------------")
        name = json.loads(jsonPerson['rutCliente']) #Se saca nombre del body

        #se crea json de respuesta
        body = {
            "PFCreaCasoSalidaResp": [
                {
                "success": true,
                "rutcliente": "16076053-2",
                "idCaso": "50001000001QnawAAC",
                "errors": ""
                }
            ],
            "PFCreaCasoSalidaReq": null
        }
        response = {
            "codigo": 200,
            "fakeResponse": json.dumps(body)
        }
        #Se inserta nombre en la tabla de personsTable
        responseInsert = table.put_item(
           Item={
                'name': name
            }
        )
        print(responseInsert)

        return response
    
    except Exception as e:
        print("----------ERROR AL AGREGAR UNA PERSONA----------")
        print(e)
        print("----------ERROR AL AGREGAR UNA PERSONA----------")
        return -1

def getAllMeasurement(event, context):
    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('measurementTable')
        
        responseQuery = table.scan()

        if 'Items' in responseQuery:
            body = responseQuery['Items']
        else:
            body = {
                "mensaje": "No existe"
            }

        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }
        print("-----------El response-----------")
        print(response)
        return response
    except Exception as e:
        print("---------El error get all---------")
        print(e)

def updatePerson(event, context):
    try:
        print("-------event-------")
        print(event)
        print("-------event-------")
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table('personsTable')

        print("-------event['body']-------")
        print(event['body'])
        print("-------event['body']-------")

        #Se obtiene el body desde el event de la funcion lambda
        jsonPerson = json.loads(event['body'])
        print("-------jsonPerson-------")
        print(jsonPerson)
        print("-------jsonPerson-------")
        print("-------name-------")
        name = jsonPerson['name'] #Se saca nombre del body
        print(name)
        print("-------name-------")
        print("-------new_name-------")
        new_name = jsonPerson['new_name'] #Se saca new_nombre del body
        print(new_name)
        print("-------new_name-------")

        response = table.update_item(
            Key={
                'name': name
            },
            UpdateExpression="set name = :n",
            ExpressionAttributeValues={
                ':n': new_name
            },
            ReturnValues="UPDATED_NEW"
        )

        return response
    except Exception as e:
        print("---------El error update---------")
        print(e)
