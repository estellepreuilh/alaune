#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib, lxml.html

def unes(targetURL):
    file = urllib.urlopen(targetURL)
    data = file.read().decode('utf8')
    file.close()
    
    doc = lxml.html.document_fromstring(data)
    article_href = doc.xpath('//article[contains(@class,"titre_une")]/a/@href') + doc.xpath('//div//article[contains(@class,"grid_6 omega img_tt_chapo")]/a/@href') + doc.xpath('//article[contains(@class,"grid_6 omega img_tt_chapo voir_plus")]/a/@href') 
    doc=lxml.html.document_fromstring(data)
    article_titles = doc.xpath('//article[contains(@class,"titre_une")]/a/h1[contains(@class,"tt3 ")]/text()')  + doc.xpath('//div//article[contains(@class,"grid_6 omega img_tt_chapo")]/a//h2[contains(@class, "tt6 ")]/text()') + doc.xpath('///article[contains(@class,"grid_6 omega img_tt_chapo voir_plus")]/a//h2[contains(@class, "tt6 ")]/text()')
   
    return zip(article_titles, article_href)