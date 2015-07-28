import util, query_data, csv, pdb
from collections import OrderedDict

#currently works with each NFL and CFB table
LEAGUES = ["NFLHC"]
YEARS = ["2014", "2015", "2016", "2017"]
TABLES = [1, 2, 3, 4, 5, 6]

max = len(LEAGUES) * len(YEARS) * len(TABLES)
current = 0

grid = [(l, y, t) for l in LEAGUES for y in YEARS for t in TABLES]
for (l, y, t) in grid:
	#use these to select the league, year, and stat table desired (1 = QB, 2 = RB, 3 = WR, 4 = DEF, 5 = K, 6 = KR)
	LEAGUE_SELECTED = l
	YEAR_SELECTED = y
	TABLE_SELECTED = t

	if l == 'NFLHC' and y == '2014' and t == 6: continue

	#build query object
	data = query_data.Data(LEAGUE_SELECTED, YEAR_SELECTED, TABLE_SELECTED)

	#get valid file name
	file_name = util.get_csv_file(data)

	#get raw player data
	table_header = util.parse_table_header(data)
	player_data = util.parse_table_data(data)

	#chunk data into lists
	players = util.chunk_player_data(player_data, len(table_header))

	#push to an ordered dictionary, then write each player record to csv
	with open(file_name, 'w') as outfile:
		writer = csv.writer(outfile)
		player_dict = []
		for player in players:
			tmp = OrderedDict()
			for index in range(len(player)):
				if type(player[index].text) is float:
					tmp[table_header[index].text] = float(player[index].text)
				else: tmp[table_header[index].text] = player[index].text.replace('-', ' - ')
			player_dict.append(tmp)

		#write header to csv
		writer.writerow(tmp.keys())

		#write data to csv
		for pl in player_dict:
			writer.writerow(pl.values())

	outfile.close()

	#track overall progress
	current += 1
	util.update_progress(100 * current / max)