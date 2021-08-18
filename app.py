from generate import generatePDF

from flask import Flask, jsonify, request
import json

# pip install -U flask-cors

# file:///D:/Fabinho/Documents/Alessandro/Programa%C3%A7%C3%A3o/Projetos/projeto-pdf-python/pdfteste.pdf

from flask_cors import CORS, cross_origin

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
@cross_origin()
def criarPDF():
	try:
		response = request.get_json()

		arquivo = response.get("filename")
		conteudo = response.get("content")

		results = generatePDF(arquivo, conteudo)

		return jsonify(results)
	except:
		print("Houve um erro ao criar o arquivo pdf\n")

		results = {
			"houveram_erros": "Sim"
		}

		return jsonify(results)

if __name__== '__main__':
    app.run(debug=True)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'