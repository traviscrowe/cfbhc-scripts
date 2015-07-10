from lxml import html
from lxml import etree
import requests
import json

POSITIONS = [('Passing', 19), ('Rushing', 17), ('Recieving', 15), ('Defensive', 18)]

#TODO: refactor to chunk player data on tr index instead of using the inefficient monstrosity below
def parseTableData(queryData):
	page = requests.get(queryData.pageLink)
	tree = etree.fromstring(page.text)
	tableData = tree.xpath(queryData.tablePath + '//tr/td')

	return tableData

def chunkPlayerData(tableData = [], cols = int):
	player = []
	players = []

	#Chunk the raw table data into individual players
	for x in range(0, len(tableData), cols):
		player = tableData[x:x+cols]
		players.append(player)

	return players

def getColCount(table = int):
	if table == 1: 
		return 20
	if table == 2: 
		return 16
	if table == 3: 
		return 15
	if table == 4: 
		return 17