from lxml import html
from lxml import etree
import requests
import json

POSITIONS = {1:20, 2:16, 3:15, 4:17}

#TODO: refactor to chunk player data on tr index instead of using the inefficient monstrosity below
def parseTableData(queryData):
	page = requests.get(queryData.pageLink)
	tree = etree.fromstring(page.text)
	tableData = tree.xpath(queryData.tablePath + '//tr/td')

	return tableData

def chunkPlayerData(tableData = [], cols = int):
	player = []
	players = []

	for x in range(0, len(tableData), cols):
		player = tableData[x:x+cols]
		players.append(player)

	return players

def getColCount(table = int):
	return POSITIONS[table]