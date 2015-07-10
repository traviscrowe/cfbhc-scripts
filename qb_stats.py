from lxml import html
from lxml import etree
from bs4 import BeautifulSoup
import requests
import urllib2
import json
import util

LEAGUES = ["NFLHC", "CFBHC"]
#currently works only with 2017 stats
YEARS = ["2014", "2015", "2016", "2017"]
TABLES = [1, 2, 3, 4, 5, 6]

LEAGUE_SELECTED = "NFLHC"
YEAR_SELECTED = "2017"
TABLE_SELECTED = "1"

WIKI_LINK = "http://cfbhc.com/wiki/index.php?title=%s_%s_Season_Stats" % (YEAR_SELECTED, LEAGUE_SELECTED)
TABLE_PATH = '//*[@id="mw-content-text"]/table[%s]' % (TABLE_SELECTED)

#Make the request and parse the result
#TODO: refactor to chunk player data on tr index instead of using the inefficient monstrosity below
page = requests.get(WIKI_LINK)
tree = etree.fromstring(page.text)
tags = tree.xpath(TABLE_PATH + '//tr/td')

player = []
players = []

#Chunk the raw table data into individual players
for x in range(0, len(tags), 20):
	player = tags[x:x+20]
	players.append(player)

#Print each list of stats for each player
for t in players:
	tmp = []
	for p in t:
		tmp.append(p.text)
	i = util.Passer(tmp)
	j = i.to_JSON()
	print j