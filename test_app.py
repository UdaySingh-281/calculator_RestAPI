import unittest
from app import app

class CalculatorTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_add(self):
        response = self.client.get('/add?a=2&b=3')
        self.assertEqual(response.json['result'], 5.0)

    def test_subtract(self):
        response = self.client.get('/subtract?a=5&b=3')
        self.assertEqual(response.json['result'], 2.0)

    def test_multiply(self):
        response = self.client.get('/multiply?a=4&b=3')
        self.assertEqual(response.json['result'], 12.0)

    def test_divide(self):
        response = self.client.get('/divide?a=10&b=2')
        self.assertEqual(response.json['result'], 5.0)

    def test_divide_by_zero(self):
        response = self.client.get('/divide?a=10&b=0')
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
