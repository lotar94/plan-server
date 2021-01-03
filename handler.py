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
        jsonRequest = json.loads(event['body'])
        print("-------------El body-------------")
        print(jsonRequest)
        print(jsonRequest['room_temperature'])
        print("-------------El body-------------")

        #room_temperature = json.loads(jsonRequest['room_temperature']) #Se saca temperatura ambiente del body
        #soil_moisture = json.loads(jsonRequest['soil_moisture']) #Se saca humedad de la tierra del body


        print("-------------Los valores2-------------")
        print(jsonRequest['room_temperature'])
        print(jsonRequest['soil_moisture'])
        print("-------------Los valores2-------------")
        
        #Se inserta nombre en la tabla de personsTable
        responseInsert = table.put_item(
            Item={
                'room_temperature': jsonRequest['room_temperature'],
                'soil_moisture': jsonRequest['soil_moisture']
            }
        )
        print(responseInsert)
        #se crea json de respuesta
        body = {
                "mensaje": "Mediciones ingresadas exitosamente"
            }

        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }
        return response
    
    except Exception as e:
        print("----------ERROR AL AGREGAR LAS MEDICIONES----------")
        print(e)
        print("----------ERROR AL AGREGAR LAS MEDICIONES----------")
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
