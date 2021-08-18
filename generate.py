from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

import os

def generatePDF(filename, content):
	diretorio = os.path.dirname(__file__)

	cnv = canvas.Canvas("{}\\{}.pdf".format(diretorio, filename), pagesize=A4)

	# As coordenadas são medidas em pontos, não em milimetros
	cnv.drawString(100, 790-100, "Olá mundo! Valor desejado: {}".format(content))
	cnv.save()

	results = {
		"local_do_arquivo": "{}\\{}.pdf".format(diretorio, filename),
		"formato": "PDF",
		"houveram_erros": "Não"
	}

	return results