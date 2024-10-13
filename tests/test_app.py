import unittest
from app.main import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Base Wallet Balance Viewer API', response.data)

    def test_balance_no_address(self):
        response = self.app.get('/balance')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Address not provided', response.data)

    def test_balance_invalid_address(self):
        response = self.app.get('/balance?address=invalid')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid address format', response.data)

    # Add more tests as needed

if __name__ == "__main__":
    unittest.main()
