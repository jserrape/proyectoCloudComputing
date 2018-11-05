import unittest
import app


class TestMyServer(unittest.TestCase):

    def test_first(self):
        response = app.index()
        self.assertIn('OK', response, "Se ha encontrado un error en index")

    def test_secondt(self):
        response = app.about()
        self.assertIn('OK', response, "Se ha encontrado un error en about")

    def test_third(self):
        response = app.form('I love you')
        self.assertIn('OK', response, "Se ha encontrado un error en analize")

    def test_fourth(self):
        response = app.form('I hate you')
        self.assertIn('NEGATIVE', response, "Se ha encontrado un error en analize")

    def test_fiveth(self):
        response = app.form('I love you')
        self.assertIn('POSITIVE', response, "Se ha encontrado un error en analize")


if __name__ == '__main__':
    unittest.main()
