from flask import Flask, jsonify, make_response, request
import logging

app = Flask(__name__)
logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s %(message)s')


@app.route("/status")
def status():
    res = {"result": "OK - healthy"}
    app.logger.info('%s endpoint was reached', request.path)
    return make_response(jsonify(res), 200)


@app.route("/metrics")
def metrics():
    res = {"data": {"UserCount": 140, "UserCountActive": 23}}
    app.logger.info('%s endpoint was reached', request.path)
    return make_response(jsonify(res), 200)


@app.route("/")
def hello():
    app.logger.info('%s endpoint was reached', request.path)
    return "Hello World"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
