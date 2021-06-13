from flask import Flask, jsonify, make_response

app = Flask(__name__)


@app.route("/status")
def status():
    res = {"result": "OK - healthy"}
    return make_response(jsonify(res), 200)


@app.route("/metrics")
def metrics():
    res = {"data": {"UserCount": 140, "UserCountActive": 23}}
    return make_response(jsonify(res), 200)


@app.route("/")
def hello():
    return "Hello World"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
