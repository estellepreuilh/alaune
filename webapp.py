# -*- coding:utf-8 -*-

from flask import Flask, request, render_template

from view import plain_html,recherche
from model import modele_donnees,model_extraction

app = Flask(__name__)

@app.route('/')
def index():
	html= recherche.recherche()
	model_extraction.extraction_all()				#pour enregistrer les titres du jour dans la base de donnée
	return render_template("index.html")+html

@app.route('/quel_journal', methods = ['POST'])
def quel_journal():
	journal = request.form['journal']
	unes= modele_donnees.select_unes(journal)
	return plain_html.htmlize_journal(unes, journal)   #ceci affiche les unes met beaucoup d'url derriere ne corresponde à aucune page, je n'ai pas réussis à régler ce soucis...


@app.route('/quel_candidat', methods = ['POST'])
def quel_candidat():
	candidat = request.form['candidat']
	unes = modele_donnees.select_candidat(candidat)
	return plain_html.htmlize_candidat(unes, candidat) #idem peu d' url correspondent à la page correspondante au titre de la une


if __name__ == '__main__':
	app.run(debug=True)

