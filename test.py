import unittest
import app


class TestMyServer(unittest.TestCase):

    def test_first(self):
        response = app.index()
        self.assertIn('OK', response, "Se ha encontrado un error en index")

if __name__ == '__main__':
    unittest.main()
