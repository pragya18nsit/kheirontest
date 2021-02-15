from flask import Flask,jsonify,request,make_response,url_for,redirect
import Calculator

import requests,json

app = Flask(__name__)


from flask import request

REST_PORT = 8080



@app.route('/calculator/v1/', methods=['POST'])
def calculator():
    if not request.json or not ('prefixExpression' in request.json or 'infixExpression' in request.json):
        abort(400)
    if request.json.get('prefixExpression'):
        expression = request.json['prefixExpression']
        print (expression)
        result = Calculator.Calc().prefix_calculator(expression)

    if request.json.get('infixExpression'):
        expression = request.json['infixExpression']
        result = Calculator.Calc().infix_calculator(expression)

    return jsonify({'response': str(result)}), 201




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=REST_PORT)
