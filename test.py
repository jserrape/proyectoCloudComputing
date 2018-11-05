import unittest
import app


class TestMyServer(unittest.TestCase):

    def test_first(self):
        response = app.index()
        self.assertIn('OK', response, "OK was not found in response")

if __name__ == '__main__':
    unittest.main()
