# -*- coding:utf-8-*-
import mysql.connector
import json
from datetime import datetime
import modele_donnees


config = json.loads(open('config.json', 'r').read())
cnx = mysql.connector.connect(** config)
cursor = cnx.cursor(buffered=True)

from extraction import CourrierInternational, LePoint, JournalduNet, LesEchos, LeDauphine, LaTribune, SudOuest, LeFigaro, LeParisien, _20minutes, LeMonde, OuestFrance

def extraction_all():
	journal={}
	journal[0]="Courrier International"
	journal[1]="Le Point"
	journal[2]= "Le Journal Du Net"
	journal[3]= "Les Echos"
	journal[4]="La Tribune"
	journal[5]="Le Dauphine"
	journal[6]="Le Monde"
	journal[7]="Ouest France"
	journal[8]="Sud Ouest"
	journal[9]="20 Minutes"
	journal[10]="Le Figaro"
	journal[11]="Le Parisien"
	for i in range(12):
		unes(journal[i])


def extraction (journal, titres, quotidien, targetURL):
	date = datetime.now().strftime('%Y-%m-%d')
	for t in titres:
		titre = t[0]
		URL = targetURL + t[1]
		une = {}
		une['date'] = date
		une['URL'] = str(URL)
		une['titre'] = titre.encode('utf8')
		modele_donnees.insert_une( une, quotidien)
	return True
	

def unes(journal):
	if journal == 'Courrier International':
		targetURL = 'http://www.courrierinternational.com'
		titres = CourrierInternational.unes(targetURL)
		quotidien={'nom':'Courrier International', 'URL':targetURL}
		extraction (journal, titres, quotidien, targetURL)
	elif journal == 'Le Point':
		targetURL = 'http://www.lepoint.fr'
		titres = LePoint.unes(targetURL)
		quotidien={'nom':'Le Point', 'URL':targetURL}
		extraction (journal, titres, quotidien, targetURL)
	elif journal == 'Le Journal Du Net':
		targetURL = 'http://www.lejournaldunet.fr'
		titres = JournalduNet.unes(targetURL)
		quotidien={'nom':'Le Journal Du Net', 'URL':targetURL}
		extraction (journal, titres, quotidien, targetURL)
	elif journal == 'Les Echos':
		targetURL = 'http://www.lesechos.fr/'
		titres = LesEchos.unes(targetURL)
		quotidien={'nom':'Les Echos', 'URL':targetURL}
		extraction (journal, titres, quotidien, targetURL)
	elif journal == 'La Tribune':
		targetURL = 'http://www.latribune.fr/'
		titres = LaTribune.unes(targetURL)
		quotidien={'nom':'La Tribune', 'URL':targetURL}
		extraction (journal, titres, quotidien,'')
	elif journal == 'Le Dauphine':
		targetURL= 'http://ledauphine.com'
		titres=LeDauphine.unes(targetURL)
		quotidien={'nom':'Le Dauphine', 'URL':targetURL}
		extraction (journal, titres, quotidien, targetURL)
	elif journal == 'Le Monde':
		targetURL = 'http://www.lemonde.fr'
		titres= LeMonde.unes(targetURL)
		quotidien={'nom':'Le Monde', 'URL':targetURL}
		extraction (journal, titres, quotidien, targetURL)
	elif journal == 'Ouest France':
		targetURL = 'http://www.ouest-france.fr'
		titres=OuestFrance.unes(targetURL)
		quotidien={'nom':'Ouest France', 'URL':targetURL}
		extraction (journal, titres, quotidien, targetURL)
	elif journal == 'Sud Ouest' :
		targetURL= 'http://www.sudouest.fr/'
		titres=SudOuest.unes(targetURL)
		quotidien={'nom':'Sud Ouest', 'URL':targetURL}
		extraction (journal, titres, quotidien, targetURL)
	elif journal == 'Figaro' :
		targetURL= 'http://www.lefigaro.fr/'
		titres=LeFigaro.unes(targetURL)
		quotidien={'nom':'Le Figaro', 'URL':targetURL}
		extraction (journal, titres, quotidien, targetURL)
	elif journal=='Le Parisien':
		targetURL='http://www.leparisien.fr'
		titres=LeParisien.unes(targetURL)
		quotidien={'nom':'Le Parisien', 'URL':targetURL}
		extraction (journal, titres, quotidien, '')
	else: # journal=='20min':
		targetURL='http://www.20minutes.fr'
		titres=_20minutes.unes(targetURL)
		quotidien={'nom':'20 minutes', 'URL':targetURL}
		extraction (journal, titres, quotidien, targetURL)



def candidat(candidat):
	if candidat == 'Fillon' :
		cursor.execute("SELECT titre,url FROM unes WHERE titre LIKE '%Fillon%' AND date >= DATE_SUB(CURDATE(), INTERVAL 3 DAY)")
		unes=cursor.fetchall()
	elif candidat == 'Macron':	
		cursor.execute("SELECT titre FROM unes WHERE titre LIKE '%Macron%' AND date >= DATE_SUB(CURDATE(), INTERVAL 3 DAY)")
		unes=cursor.fetchall()
	elif candidat == 'Aignan' :
		cursor.execute("SELECT titre FROM unes WHERE titre LIKE '%Dupont Aignan%' AND date >= DATE_SUB(CURDATE(), INTERVAL 3 DAY)")
		unes=cursor.fetchall()
	elif candidat == 'Asselineau' :
		cursor.execute("SELECT titre FROM unes WHERE titre LIKE '%Asselineau%' AND date >= DATE_SUB(CURDATE(), INTERVAL 3 DAY)")
		unes=cursor.fetchall()
	elif candidat == 'Le Pen' : 
		cursor.execute("SELECT titre FROM unes WHERE titre LIKE '%Le n Pen%' AND date >= DATE_SUB(CURDATE(), INTERVAL 3 DAY)")
		unes=cursor.fetchall()
	elif candidat == 'Poutou' :
		cursor.execute("SELECT titre FROM unes WHERE titre LIKE '%Poutou%' AND date >= DATE_SUB(CURDATE(), INTERVAL 3 DAY)")
		unes=cursor.fetchall()
	elif candidat == 'Melanchon' :
		cursor.execute("SELECT titre FROM unes WHERE titre LIKE '%Melanchon%' AND date >= DATE_SUB(CURDATE(), INTERVAL 3 DAY)")
		unes=cursor.fetchall()
	elif candidat == 'Cheminade' :
		cursor.execute("SELECT titre FROM unes WHERE titre LIKE '%Cheminade%' AND date >= DATE_SUB(CURDATE(), INTERVAL 3 DAY)")
		unes=cursor.fetchall()
	elif candidat == 'Arthaud' :
		cursor.execute("SELECT titre FROM unes WHERE titre LIKE '%Arthaud%' AND date >= DATE_SUB(CURDATE(), INTERVAL 3 DAY)")
		unes=cursor.fetchall()
	elif candidat == 'Hamon' :
		cursor.execute("SELECT titre FROM unes WHERE titre LIKE '%Hamon%' AND date >= DATE_SUB(CURDATE(), INTERVAL 3 DAY)")
		unes=cursor.fetchall()
	else : # candidat == 'Lassalle' 
		cursor.execute("SELECT titre FROM unes WHERE titre LIKE '%Lassalle%' AND date >= DATE_SUB(CURDATE(), INTERVAL 3 DAY)")
		unes=cursor.fetchall()
	return unes

if __name__ == '__main__':
	print True



