import models
import util
import query_data
import json

#currently only works with NFLHC in 2017 due to table changes from CFB -> NFLHC in that year
LEAGUES = ["NFLHC"]
YEARS = ["2017"]
TABLES = [1, 2, 3, 4, 5, 6]

LEAGUE_SELECTED = LEAGUES[0]
YEAR_SELECTED = YEARS[0]
TABLE_SELECTED = TABLES[3]

#build query object
data = query_data.Data(LEAGUE_SELECTED, YEAR_SELECTED, TABLE_SELECTED)

#get raw player data
player_data = util.parse_table_data(data)

#chunk data into lists
players = util.chunk_player_data(player_data, data.cols)

final = []

#serialize to json and print each list of stats for each player
for t in players:
	tmp = []
	for p in t:
		tmp.append(p.text)
	i = models.Defender(tmp)
	print i.to_JSON()
