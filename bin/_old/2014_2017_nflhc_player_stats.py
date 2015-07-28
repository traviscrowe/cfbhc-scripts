import models, util, query_data, json, csv, pdb, string
from collections import OrderedDict

#currently only works with NFLHC in 2017 due to table changes from CFB -> NFLHC in that year
LEAGUES = ["CFBHC", "NFLHC"]
YEARS = ["2014", "2015", "2016", "2017"]
TABLES = [1, 2, 3, 4, 5, 6]

#use these to select the league, year, and stat table desired (1 = QB, 2 = RB, 3 = WR, 4 = DEF, 5 = K, 6 = KR)
LEAGUE_SELECTED = LEAGUES[1]
YEAR_SELECTED = YEARS[3]
TABLE_SELECTED = TABLES[0]

#build query object
data = query_data.Data(LEAGUE_SELECTED, YEAR_SELECTED, TABLE_SELECTED)

#get raw player data
table_header = util.parse_table_header(data)
player_data = util.parse_table_data(data)

#chunk data into lists
players = util.chunk_player_data(player_data, len(table_header))

count = 0
#push to an ordered dictionary, then write each player record to csv
with open(util.get_csv_file(query_data), 'w') as outfile:
	writer = csv.writer(outfile)
	player_dict = []
	for player in players:
		tmp = OrderedDict()
		for index in range(len(player)):
			if type(player[index].text) is float:
				tmp[table_header[index].text] = float(player[index].text)
			else: tmp[table_header[index].text] = player[index].text.replace('-', ' - ')
		player_dict.append(tmp)

	writer.writerow(tmp.keys())

	for pl in player_dict:
		writer.writerow(pl.values())

	count += 1

if(count == 0): print("No stats...")
