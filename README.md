INSTALLATION STEPS
**********************
1. Set up Python version 3.7.5
2. Run command pip -r requirements.txt

EXECUTION STEPS
***************

To run as a web server

1. Set rest port in webapp.py
2. cd webapp. Run command python3 webapp.py

Run as a standalone application

1. Run python3 input_calculator.py to execute as a standalone application.

TEST CASES
***********
1. Calculator_test.py contains unit tests for calculator in standalone mode.
2. webproject/app_test.py contains unit tests for calculator in webapp.

CURL COMMANDS
******************
For Prefix Expression:

curl -X POST \
  http://0.0.0.0:8081/calculator \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{"prefixExpression" : "+ 1 2"}'


For Infix Expression:
curl -X POST \
  http://0.0.0.0:8081/calculator \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: 81ac1bbd-cb48-0ead-3542-e9fe33cf1c48' \
  -d '{"infixExpression" : "1 + 2"}'
