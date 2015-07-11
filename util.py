from lxml import html
from lxml import etree
import requests
import json

POSITIONS = {1:20, 2:16, 3:15, 4:17}

#TODO: refactor to chunk player data on tr index instead of using the inefficient monstrosity below
def parse_table_data(query_data):
	page = requests.get(query_data.page_link)
	tree = etree.fromstring(page.text)
	table_data = tree.xpath(query_data.table_path + '//tr/td')

	return table_data

def chunk_player_data(table_data = [], cols = int):
	player = []
	players = []

	for x in range(0, len(table_data), cols):
		player = table_data[x:x+cols]
		players.append(player)

	return players

def get_col_count(table = int):
	return POSITIONS[table]