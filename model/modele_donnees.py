#! /usr/bin/python
# -*- coding:utf-8 -*-
import mysql.connector
import json

config = json.loads(open('config.json', 'r').read())
cnx = mysql.connector.connect(** config)
cursor = cnx.cursor(buffered=True)


def insert_quotidien( quotidien):
	cursor.execute("SELECT nom FROM quotidien WHERE nom LIKE (%(nom)s)", quotidien)
	if (cursor.rowcount==0):
		add_quotidien = ("INSERT INTO quotidien (nom, URL) VALUES (%(nom)s, %(URL)s)")
		cursor.execute(add_quotidien, quotidien)
		cnx.commit()


def insert_une(une, quotidien):
	cursor.execute("SELECT titre FROM unes WHERE titre LIKE (%(titre)s)", une)
	if (cursor.rowcount==0):
		quotidien_id = ("SELECT id FROM quotidien WHERE nom LIKE (%(nom)s)")
		cursor.execute(quotidien_id, quotidien)		
		quot_id = cursor.fetchone()
		une['quotidien_id'] = quot_id[0]
		add_une = ("INSERT INTO unes (id, titre, URL, date, quotidien_id) VALUES (NULL,%(titre)s, %(URL)s, %(date)s, %(quotidien_id)s)")
		cursor.execute(add_une, une)
		cnx.commit()


def select_quotidien(quotidien):
	get_quotidien = ("SELECT id FROM quotidien WHERE nom LIKE '%" + quotidien + "%'")
	cursor.execute(get_quotidien)
	id = cursor.fetchone()[0]
	return id


def select_unes(quotidien):
	quotidien_id = select_quotidien(quotidien)
	print quotidien_id
	get_unes = ("SELECT titre, URL FROM unes WHERE quotidien_id LIKE " + str(quotidien_id) + " AND date >= DATE_SUB(CURDATE(), INTERVAL 2 DAY)")
	print get_unes
	cursor.execute(get_unes)
	if cursor.rowcount == 0:
		return None
	else:
		unes = cursor.fetchall()
		return unes

		
def select_candidat(candidat):
	cursor.execute ("SELECT titre, URL FROM unes WHERE titre LIKE '%" + candidat + "%' AND date >= DATE_SUB(CURDATE(), INTERVAL 3 DAY) ORDER BY date DESC ")
	if cursor.rowcount == 0:
		une={}
		return une
	else:
		unes = cursor.fetchall()
		return unes