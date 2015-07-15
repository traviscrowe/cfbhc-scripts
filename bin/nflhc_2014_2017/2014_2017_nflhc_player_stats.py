import models, util, query_data, json

#currently only works with NFLHC in 2017 due to table changes from CFB -> NFLHC in that year
LEAGUES = ["NFLHC"]
YEARS = ["2014", "2017"]
TABLES = [1, 2, 3, 4, 5, 6]

#use these to select the league, year, and stat table desired (1 = QB, 2 = RB, 3 = WR, 4 = DEF, 5 = K, 6 = KR)
LEAGUE_SELECTED = LEAGUES[0]
YEAR_SELECTED = YEARS[0]
TABLE_SELECTED = TABLES[3]

#build query object
data = query_data.Data(LEAGUE_SELECTED, YEAR_SELECTED, TABLE_SELECTED)

#get raw player data
player_data = util.parse_table_data(data)

#chunk data into lists
players = util.chunk_player_data(player_data, data.cols)

count = 0
#serialize to json and print each list of stats for each player
for t in players:
	tmp = []
	for p in t:
		tmp.append(p.text)
	i = util.get_player_model_by_key(TABLE_SELECTED, tmp)
	print i.to_JSON()
	count += 1
if(count == 0): print "No stats..."
