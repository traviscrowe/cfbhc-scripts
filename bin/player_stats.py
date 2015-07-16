import models, util, query_data, json, csv

#currently only works with NFLHC in 2017 due to table changes from CFB -> NFLHC in that year
LEAGUES = ["NFLHC", "CFBHC"]
YEARS = ["2014", "2015", "2016", "2017"]
TABLES = [1, 2, 3, 4, 5, 6]
DATA_TYPE = ["JSON", "CSV"]

#use these to select the league, year, and stat table desired (1 = QB, 2 = RB, 3 = WR, 4 = DEF, 5 = K, 6 = KR)
LEAGUE_SELECTED = LEAGUES[0]
YEAR_SELECTED = YEARS[1]
TABLE_SELECTED = TABLES[0]
DATA_TYPE_SELECTED = DATA_TYPE[1]

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
	data = util.get_player_model_by_key(TABLE_SELECTED, tmp)
	l = data.load_JSON()
	final.append(l)

#this sucks, a lot
meh = str(final)
meh = meh.replace('\'', '"')

print meh