from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from flask import Flask, jsonify, request
import json

import os

# pip install -U flask-cors

# file:///D:/Fabinho/Documents/Alessandro/Programa%C3%A7%C3%A3o/Projetos/projeto-pdf-python/pdfteste.pdf

from flask_cors import CORS, cross_origin

app = Flask(__name__)

@app.route('/test', methods=['POST'])
@cross_origin()
def criarPDF():
	try:
		response = request.get_json()

		arquivo = response.get("filename")
		conteudo = response.get("content")

		diretorio = os.path.dirname(__file__)

		cnv = canvas.Canvas("{}\\{}.pdf".format(diretorio, arquivo), pagesize=A4)

		# As coordenadas são medidas em pontos, não em milimetros
		cnv.drawString(100, 790-100, "Olá mundo! Valor desejado: {}".format(conteudo))
		cnv.save()

		results = {
			"local_do_arquivo": "{}\\{}.pdf".format(diretorio, arquivo),
			"formato": "PDF",
			"houveram_erros": "Não"
		}

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