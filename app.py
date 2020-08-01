from flask import Flask, request, jsonify

app = Flask(__name__)

measurement = ['sin Informacion']

@app.route('/')
def hello():
    return 'Hola que hace'

@app.route('/getData')
def getData():
    return measurement[0]


@app.route('/lastMeasurement', methods=['POST'])
def saveLastMeasurement():
    data = request.json
    measurement[0] = data
    print(measurement)
    return jsonify({"message": "data ingresa exitosamente"})
