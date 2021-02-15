INSTALLATION STEPS
**********************
1. Set up Python version 3.7.5
2. Run command pip -r requirements.txt

EXECUTION STEPS
***************

To run as a web server

1. Set rest port in app.py
2. Run command python app.py

To run as a standalone application
1. Run python calculator.py


TEST CASES
***********
1. Calculator_test.py contains unit tests for calculator in standalone mode.
2. Calculator rest_test.py contains unit tests for calculator in webapp.

CURL COMMANDS
******************
For Prefix Expression:

curl -X POST \
  http://0.0.0.0:105/calculator \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{"prefixExpression" : "+ 1 2"}'


For Infix Expression:
curl -X POST \
  http://0.0.0.0:105/calculator \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: 81ac1bbd-cb48-0ead-3542-e9fe33cf1c48' \
  -d '{"infixExpression" : "1 + 2"}'
