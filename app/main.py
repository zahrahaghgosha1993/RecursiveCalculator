import flask
from flask import jsonify, request

from calculator.ackerman_calculator import AckermanCalculator
from calculator.factorial_calculator import FactorialCalculator
from calculator.fibonacci_calculator import FibonacciCalculator
from utils.get_redis_client import get_redis_client

from utils.exeptions import JsonValidationError
from utils.validations import validate_schema

app = flask.Flask(__name__)

r = get_redis_client()
r.hmset('Fibonacci', {"0": 0, "1": 1, "2": 1})
r.hmset('Factorial', {"0": 1, "1": 1, "2": 2})

schema = {
    "type": "object",
    "properties": {
        "n": {
            "type": "integer",
            "minimum": 0
        },
        "function": {
            "type": "string"
        }
    },
    "required": ["n", "function"]
}


@app.errorhandler(JsonValidationError)
def validation_error(e):
    return jsonify({'error': e.message, 'errors': [validation_error.message for validation_error in e.errors]}), 400


@app.errorhandler(NotImplementedError)
def validation_error(e):
    return jsonify({'error': "requested function not implemented"}), 501


@app.route('/recursive_calculator/', methods=['POST'])
@validate_schema(schema=schema)
def recursive_calculator():
    n = request.json["n"]
    function = request.json["function"]
    result = r.hget(function, str(n))
    if result:
        return jsonify({"result": result.decode("utf-8")}), 200

    strategies = {
        "Fibonacci": FibonacciCalculator(),
        "Factorial": FactorialCalculator()
    }

    Calculator = strategies.get(function)
    if Calculator:
        result = Calculator.calculate(n)
        return jsonify({"result": result}), 200
    else:
        raise NotImplementedError


@app.route('/ackerman_calculator/', methods=['POST'])

def ackerman_calculator():
    n = request.json["n"]
    m = request.json["m"]

    a= AckermanCalculator()
    result = a.ackerman(m=m, n=n)
    if result:
        return jsonify({"result": result}), 200
    else:
        raise NotImplementedError


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=5000)
