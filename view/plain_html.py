# -*- coding:utf-8 -*-

def htmlize(titles_and_href, targetURL):
	html = ''
	html += '<link href="{{ url_for("static", filename="style.css") }}" rel="stylesheet" type="text/css" />'
	for item in titles_and_href:
		html += '<h2>'
		html += '<a href="' + targetURL + item[1] + '">' + item[0].strip() + '</a></h2>\n'
	return html

def htmlize_candidat(une,candidat):
	html = ''
	html += '<h2> Voici les unes depuis 3 jours correspondantes au candidat : '+ candidat + '</h2><br/>'
	html += '<link href="/static/style.css" rel="stylesheet" type="text/css" /> '
	html += '<ul>' 
	if len(une)==0:
		html += 'Il n\'y a pas eu de une sur ce candidat ces derniers jours.'
	else :
		for item in une:
			html += '<h3>'
			html += '<li><a href="' + item[1] + '">' + item[0].strip() + '</li></h3>\n'
	html += '</ul>'
	return html

def htmlize_journal(une,journal):
	html = ''
	html += '<h2> Voici les unes d\'aujourd\'hui et d\'hier correspondantes au journal : '+ journal + '</h2><br/>'
	html += '<link href="/static/style.css" rel="stylesheet" type="text/css" />  '
	html += '<ul>' 
	for item in une:
		html += '<h3>'
		html += '<li> <a href="' + item[1] + '">' + item[0].strip() + '</li></h3>\n'
	html += '</ul>'
	return html