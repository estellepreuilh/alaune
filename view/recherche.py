# !/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, request, render_template
import mysql.connector
import json

config = json.loads(open('config.json', 'r').read())
cnx = mysql.connector.connect(** config)
cursor = cnx.cursor(buffered=True)


def recherche():
	cursor.execute("SELECT titre,date FROM unes WHERE titre LIKE '%Fillon%' AND date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)")
	une=cursor.fetchall()
	nbFil=len(une)
	cursor.execute("SELECT titre FROM unes WHERE titre LIKE '%Macron%' AND date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)")
	une=cursor.fetchall()
	nbMac=len(une)
	cursor.execute("SELECT titre FROM unes WHERE titre LIKE '%Dupont Aignan%' AND date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)")
	une=cursor.fetchall()
	nbDuA=len(une)
	cursor.execute("SELECT titre FROM unes WHERE titre LIKE '%Asselineau%' AND date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)")
	une=cursor.fetchall()
	nbAss=len(une)
	cursor.execute("SELECT titre FROM unes WHERE titre LIKE '%Le Pen%' AND date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)")
	une=cursor.fetchall()
	nbPen=len(une)
	cursor.execute("SELECT titre FROM unes WHERE titre LIKE '%Poutou%' AND date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)")
	une=cursor.fetchall()
	nbPou=len(une)
	cursor.execute("SELECT titre FROM unes WHERE titre LIKE '%Melenchon%' AND date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)")
	une=cursor.fetchall()
	nbMel=len(une)
	cursor.execute("SELECT titre FROM unes WHERE titre LIKE '%Cheminade%' AND date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)")
	une=cursor.fetchall()
	nbChe=len(une)
	cursor.execute("SELECT titre FROM unes WHERE titre LIKE '%Arthaud%' AND date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)")
	une=cursor.fetchall()
	nbArt=len(une)
	cursor.execute("SELECT titre FROM unes WHERE titre LIKE '%Hamon%' AND date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)")
	une=cursor.fetchall()
	nbHam=len(une)
	cursor.execute("SELECT titre FROM unes WHERE titre LIKE '%Lassalle%' AND date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)")
	une=cursor.fetchall()
	nbLas=len(une)
	nb= nbFil + nbMac + nbDuA + nbAss + nbPen + nbPou + nbMel + nbChe + nbArt + nbHam + nbLas

	html = ' '
	html += '<script>\n'
	html += 'parm=[{"label":"Fillon", "value": ' + str(nbFil) + '},'
	html += '{"label":"Macron", "value": ' + str(nbMac) + '},'
	html += '{"label":"Aignan", "value": ' + str(nbDuA) + '},'
	html += '{"label":"Asselineau", "value": ' + str(nbAss) + '},'
	html += '{"label":"Le Pen", "value": ' + str(nbPen) + '},'
	html += '{"label":"Poutou", "value": ' + str(nbPou) + '},'
	html += '{"label":"Melanchon", "value": ' + str(nbMel) + '},'
	html += '{"label":"Cheminade", "value": ' + str(nbChe) + '},'
	html += '{"label":"Arthaud", "value": ' + str(nbArt) + '},'
	html += '{"label":"Hamon", "value": ' + str(nbHam) + '},'
	html += '{"label":"Lassalle", "value": ' + str(nbLas) + '}];\n'
	html += 'nb=' + str(nb) + ';\n'
	html += 'piechart(parm, nb);\n'
	html += '</script>\n'
	html += '</body>\n'
	html += '</html>\n'
	cnx.commit()
	return html


if __name__ == '__main__':
	recherche()
	
	
	
	
	## <link href="{{url_for('static', filename='style.css')}}" rel=