import models
import util
import query_data

LEAGUES = ["NFLHC"]
YEARS = ["2017"]
TABLES = [1, 2, 3, 4, 5, 6]

LEAGUE_SELECTED = "NFLHC"
YEAR_SELECTED = "2017"
TABLE_SELECTED = 4

data = query_data.Data(LEAGUE_SELECTED, YEAR_SELECTED, TABLE_SELECTED)

playerData = util.parseTableData(data)

print data.league
print data.tablePath
print data.pageLink
print data.cols

players = util.chunkPlayerData(playerData, data.cols)

#Print each list of stats for each player
for t in players:
	tmp = []
	for p in t:
		tmp.append(p.text)
	i = models.Defender(tmp)
	j = i.to_JSON()
	print j