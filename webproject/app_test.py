import unittest
import json
from webapp import app

class TestApp(unittest.TestCase):
    def test_app(self):

        app_client = app.test_client()


        #TEST CASES FOR prefix EXPRESSIONS#
        payload1 = {
            "prefixExpression": "+ 1 * 2 3"
        }


        res = app_client.post('/v1/calculator',json=payload1,follow_redirects=True)

        self.assertEqual(res.status_code, 201)
        self.assertEqual(int(json.loads(res.data)['response']), 7)


        payload2 = {
            "prefixExpression": "+ * 1 2 3"
        }


        res = app_client.post('/v1/calculator',json=payload2,follow_redirects=True)

        self.assertEqual(res.status_code, 201)
        self.assertEqual(int(json.loads(res.data)['response']), 5)

        #=============TEST CASES FOR PREFIX ENDS===========#

        #TEST CASES FOR INFIX EXPRESSIONS#
        payload3 = {
            "infixExpression": "( ( 1 * 2 ) + 3 )"
        }


        res = app_client.post('/v1/calculator',json=payload3,follow_redirects=True)

        self.assertEqual(res.status_code, 201)
        self.assertEqual(int(json.loads(res.data)['response']), 5)


        payload4 = {
            "infixExpression": "( 1 + 2 )"
        }


        res = app_client.post('/v1/calculator',json=payload4,follow_redirects=True)

        self.assertEqual(res.status_code, 201)
        self.assertEqual(int(json.loads(res.data)['response']), 3)


if __name__ == '__main__':
    unittest.main()
