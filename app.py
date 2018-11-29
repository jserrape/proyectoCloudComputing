from flask import Flask, jsonify, request, Response
from nltk.tokenize import TreebankWordTokenizer
from nltk import WhitespaceTokenizer, SpaceTokenizer, WordPunctTokenizer, TreebankWordTokenizer

import io, nltk, sys, time, numpy, os, json


app = Flask(__name__)
PORT = 80
DEBUG = False

#Otros
_POS_TAGGER = 'taggers/maxent_treebank_pos_tagger/english.pickle'

#Valores
sustantivos=1
adjetivos=1.8
verbos=0.8
adverbios= 0.95
subidaFrase=0.05


def analizar(comentario):
    listaNegativas = load_words("words/negative-words.txt")
    listaPositivas = load_words("words/positive-words.txt")
    Vfrase=1
    frases = load_frases_opinion(comentario)
    acumula=0
    for frase in frases:
        Vfrase += subidaFrase
        acumula += rate_sentence(frase,Vfrase,listaNegativas,listaPositivas)
    if(acumula > 0):
        return ("POSITIVE")
    if(acumula < 0):
        return "NEGATIVE"
    if(acumula == 0):
        return "NEUTRAL"
    return "Nunca llega"

#Carga los ficheros de palabras positivas y negativas y devuelve un array con ellas
def load_words(fichero):
    tokenizer = TreebankWordTokenizer()
    with io.open(fichero, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read().lower()
        f.close()
    return tokenizer.tokenize(text)

#Tokeniza las frases de un texto
def load_frases_opinion(texto):
    sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    return sentence_tokenizer.tokenize(texto)


#Mide el porcentaje de positividad de una frase
def rate_sentence(sentence,Vfrase,listaNegativas,listaPositivas):
    negadores=[]
    valor = 0
    tokenizer = TreebankWordTokenizer()
    tagger = nltk.data.load(_POS_TAGGER)
    tags = tagger.tag(tokenizer.tokenize(sentence))
    for i in tags:
        if (i[1] == 'NN') or (i[1] == 'NNS') or (i[1] == 'NNP') or (i[1] == 'NNPS'):
            valor += calcularValorPalabra(i[0],"sust","N",Vfrase,listaNegativas,listaPositivas)
        if (i[1] == 'JJ' or (i[1] == 'JJR') or (i[1] == 'JJS')):
            valor += calcularValorPalabra(i[0],"adj","N",Vfrase,listaNegativas,listaPositivas)
        if (i[1] == 'VB' or (i[1] == 'VBD') or (i[1] == 'VBG') or (i[1] == 'VBN') or (i[1] == 'VBP') or (i[1] == 'VBZ')):
            valor += calcularValorPalabra(i[0],"verb","N",Vfrase,listaNegativas,listaPositivas)
        if (i[1] == 'RB' or (i[1] == 'RBR') or (i[1] == 'RBS')):
            valor += calcularValorPalabra(i[0],"adv","N",Vfrase,listaNegativas,listaPositivas)
    return valor


#Calcula el valor de una palabra, en funcion de su tipo y de si esta negada
def calcularValorPalabra(palabra,tipo,negada,Vfrase,listaNegativas,listaPositivas):
    if(palabra in listaNegativas):
        return calcularValorPalabra2(tipo,"N",Vfrase)
    elif(palabra in listaPositivas):
        return calcularValorPalabra2(tipo,"Y",Vfrase)
    return 0


#Calcula el valor de un tipo de palabra en función de si está negada
def calcularValorPalabra2(tipo,positiva,Vfrase):
    if(tipo == "sust" and positiva == "Y"):
        return Vfrase*sustantivos
    elif(tipo == "sust" and positiva == "N"):
        return (Vfrase*sustantivos*(-1))

    if(tipo == "adj" and positiva == "Y"):
        return Vfrase*adjetivos
    elif(tipo == "adj" and positiva == "N"):
        return (Vfrase*adjetivos*(-1))

    if(tipo == "verb" and positiva == "Y"):
        return Vfrase*verbos
    elif(tipo == "verb" and positiva == "N"):
        return (Vfrase*verbos*(-1))

    if(tipo == "adv" and positiva == "Y"):
        return Vfrase*adverbios
    elif(tipo == "adv" and positiva == "N"):
        return (Vfrase*adverbios*(-1))
    return 0


@app.errorhandler(404)
def not_found(error):
    respons = {}
    respons['status'] = 404
    respons = jsonify(respons)
    respons.status_code = 404
    return respons

@app.route('/')
def index():
    respons = {}
    respons['status'] = 'OK'
    respons['ruta'] = '/'
    ejemplo = {}
    ejemplo['ruta'] = '/analize/I%20love%20you'
    ejemplo['valor'] = '{"ruta":"/analize/I%20love%20you","status":"OK","valor":"POSITIVE"}'
    respons['ejemplo'] = ejemplo
    respons = jsonify(respons)
    respons.status_code = 201
    return respons

@app.route('/about')
def about():
    respons = {}
    respons['status'] = 'OK'
    respons['ruta'] = '/about'
    respons['valor'] = 'Service developed by Juan Carlos Serrano Perez, source code in https://github.com/xenahort/proyectoCloudComputing'
    respons = jsonify(respons)
    respons.status_code = 201
    return respons

@app.route('/analize/<post_id>', methods=['GET', 'POST'])
def form(post_id):
    resultado = analizar(post_id)
    urr = str(post_id).replace(" ", "%20")

    respons = {}
    respons['status'] = 'OK'
    respons['ruta'] = '/analize/'+urr
    respons['valor'] = resultado
    respons = jsonify(respons)
    respons.status_code = 201

    return respons

if __name__ == '__main__':
	app.run(port = PORT, debug = DEBUG)
