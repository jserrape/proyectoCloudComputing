import unittest
import app


class TestMyServer(unittest.TestCase):

    def test_1(self):
        response = app.analizar("I hate you")
        self.assertEqual('NEGATIVE', response, "Se ha encontrado un error en analizar(<comentario1>)")

    def test_2(self):
        response = app.analizar("I love you")
        self.assertEqual('POSITIVE', response, "Se ha encontrado un error en analizar(<comentario2>)")

    def test_3(self):
        response = app.load_words("words/negative-words.txt")
        self.assertIsNotNone(response, "Se ha encontrado un error en la lectura de negative-words.txt")

    def test_4(self):
        response = app.load_words("words/positive-words.txt")
        self.assertIsNotNone(response, "Se ha encontrado un error en la lectura de positive-words.txt")

    def test_5(self):
        response = app.load_frases_opinion("Good morning, this is a test. This is another phrase.")
        self.assertIn('Good morning, this is a test.', response, "Se ha encontrado un error en la separacion de frases 1")

    def test_6(self):
        response = app.load_frases_opinion("Good morning, this is a test. This is another phrase.")
        self.assertIn('This is another phrase.', response, "Se ha encontrado un error en la separacion de frases 2")

    def test_7(self):
        response = app.rate_sentence("I hate you",1,app.load_words("words/negative-words.txt"),app.load_words("words/positive-words.txt"))
        self.assertEqual(-0.8, response, "Se ha encontrado un error en medir la positividad de una frase 1")

    def test_8(self):
        response = app.rate_sentence("I love you",1,app.load_words("words/negative-words.txt"),app.load_words("words/positive-words.txt"))
        self.assertEqual(0.8, response, "Se ha encontrado un error en medir la positividad de una frase 2")

    def test_9(self):
        response = app.calcularValorPalabra("hate","verb","N",1,app.load_words("words/negative-words.txt"),app.load_words("words/positive-words.txt"))
        self.assertEqual(-0.8, response, "Se ha encontrado un error en medir la positividad de una palabra 1")

    def test_9(self):
        response = app.calcularValorPalabra("love","verb","N",1,app.load_words("words/negative-words.txt"),app.load_words("words/positive-words.txt"))
        self.assertEqual(0.8, response, "Se ha encontrado un error en medir la positividad de una palabra 2")

    def test_10(self):
        response = app.calcularValorPalabra2("verb","Y",1)
        self.assertEqual(0.8, response, "Se ha encontrado un error en medir la positividad de una palabra 3")

    def test_11(self):
        response = app.calcularValorPalabra2("verb","N",1)
        self.assertEqual(-0.8, response, "Se ha encontrado un error en medir la positividad de una palabra 4")

    def test_12(self):
        response = app.divideOracion("I hate you")
        self.assertEqual("[('I', 'PRP'), ('hate', 'VBP'), ('you', 'PRP')]", response, "Se ha encontrado un error al dividir una oracion 1")

    def test_13(self):
        response = app.divideOracion("I am a long phrase test to analyze")
        self.assertEqual("[('I', 'PRP'), ('am', 'VBP'), ('a', 'DT'), ('long', 'JJ'), ('phrase', 'NN'), ('test', 'NN'), ('to', 'TO'), ('analyze', 'VB')]", response, "Se ha encontrado un error al dividir una oracion 2")

    def test_14(self):
        response = app.lowerr("HOLA MUNDO")
        self.assertEqual("hola mundo", response, "Se ha encontrado un error en al masar a minuscula")

    def test_15(self):
        response = app.upperr("hola mundo")
        self.assertEqual("HOLA MUNDO", response, "Se ha encontrado un error al pasar a mayuscula")



if __name__ == '__main__':
    unittest.main()
