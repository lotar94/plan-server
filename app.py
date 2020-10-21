from flask import Flask, request, jsonify
import os.path

app = Flask(__name__)

measurement = ['sin Information']

@app.route('/')
def hello():
    return 'Hola que hace!!'


@app.route('/getData')
def getData(): return measurement[0]


@app.route('/lastMeasurement', methods=['POST'])
def saveLastMeasurement():
    data = request.json
    print("1")
    validateUser(str(data["user_id"]))
    print("3")
    measurement[0] = data
    return jsonify({"message": "data ingresa exitosamente"})


def validateUser(userId):
    print("El user id: " + str(userId))
    if os.path.isfile(userId+".csv"):
        print("Existe")
    else:
        print("No existe")
        f = open(userId+".csv", "w+")
        for i in range(10):
            f.write("This is line %d\r\n" % (i + 1))
    print("2")


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
