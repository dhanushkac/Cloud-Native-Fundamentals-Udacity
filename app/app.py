from flask import Flask, jsonify, make_response, request
from datetime import datetime
import logging

app = Flask(__name__)
logging.basicConfig(filename='app.log', level=logging.DEBUG)


@app.route("/status")
def status():
    res = {"result": "OK - healthy"}
    log()
    return make_response(jsonify(res), 200)


@app.route("/metrics")
def metrics():
    res = {"data": {"UserCount": 140, "UserCountActive": 23}}
    log()
    return make_response(jsonify(res), 200)


@app.route("/")
def hello():
    log()
    return "Hello World"


def log():
    now = datetime.now()
    timestamp = int(datetime.timestamp(now))

    app.logger.info('%s, %s endpoint was reached', timestamp, request.path)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
