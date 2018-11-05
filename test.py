import unittest
import app


class TestMyServer(unittest.TestCase):

    def test_first(self):
        response = app.index()
        self.assertIn('OK', response, "Se ha encontrado un error en index")

    def test_secondt(self):
        response = app.about()
        self.assertIn('OKa', response, "Se ha encontrado un error en about")

if __name__ == '__main__':
    unittest.main()
