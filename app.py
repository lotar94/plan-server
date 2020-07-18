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

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
