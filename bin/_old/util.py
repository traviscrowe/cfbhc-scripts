from lxml import html, etree
import requests, json, models

POSITIONS = {1:20, 2:16, 3:15, 4:17, 5:16, 6:10}

#TODO: refactor to chunk player data on tr index instead of using the inefficient monstrosity below
def parse_table_data(query_data):
	page = requests.get(query_data.page_link)
	tree = etree.fromstring(page.text)
	table_data = tree.xpath(query_data.table_path + '//tr/td')

	return table_data

def parse_table_header(query_data):
	page = requests.get(query_data.page_link)
	tree = etree.fromstring(page.text)
	table_header = tree.xpath(query_data.table_path + '//th')

	return table_header

def chunk_player_data(table_data = [], cols = int):
	players = []

	for x in range(0, len(table_data), cols):
		player = table_data[x:x+cols]
		players.append(player)

	return players

def get_csv_file(query_data):
	return 'quarterbacks.csv';

#Deprecated
def get_col_count(table = int):
	return POSITIONS[table]

#Deprecated
def get_player_model_by_key(key = int, raw_data = []):
	if(key == 1):
		return models.Passer(raw_data)
	elif(key == 2):
		return models.Runner(raw_data)
	elif(key == 3):
		return models.Reciever(raw_data)
	elif(key == 4):
		return models.Defender(raw_data)
	elif(key == 5):
		return models.Kicker(raw_data)
	elif(key == 6):
		return models.Returner(raw_data)

#Deprecated
def parse_table_data_by_row(query_data):
	page = requests.get(query_data.page_link)
	tree = etree.fromstring(page.text)
	table_data = tree.xpath(query_data.table_path + '//tr/td')
	row_count = len(table_data/query_data.cols)
	players = []
	for x in range(0, row_count):
		row_data = tree.xpath(query_data.table_path + '//tr[' + x + ']')
		for rd in row_data:
			print(rd.text)