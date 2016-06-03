"""
Primary parsing script - fetches 2014 - 2018 CFBHC and NFLHC stats from the wiki
"""
from collections import OrderedDict
import csv
import util
import query_data


LEAGUES = ["CFBHC", "NFLHC"]
YEARS = ["2014", "2015", "2016", "2017", "2018"]
TABLES = [1, 2, 3, 4, 5, 6]

PARAMS = [(l, y, t) for l in LEAGUES for y in YEARS for t in TABLES]
for (l, y, t) in PARAMS:
	# Use these to select the league, year, and stat table desired
    # (1 = QB, 2 = RB, 3 = WR, 4 = DEF, 5 = K, 6 = KR)
    LEAGUE_SELECTED = l
    YEAR_SELECTED = y
    TABLE_SELECTED = t

    if l == 'NFLHC' and y == '2014' and t == 6:
        continue

    # Build query object
    data = query_data.Data(LEAGUE_SELECTED, YEAR_SELECTED, TABLE_SELECTED)

    # Get valid file name
    file_name = util.get_csv_file(data)

    # Get raw player data
    table_header = util.parse_table_header(data)
    player_data = util.parse_table_data(data)

    # Chunk data into lists
    if len(table_header) == 0:
        continue

    players = util.chunk_player_data(player_data, len(table_header))

    # Push to an ordered dictionary, then write each player record to csv
    with open(file_name, 'w') as outfile:
        writer = csv.writer(outfile)
        player_dict = []
        for player in players:
            tmp = OrderedDict()
            for index, player in enumerate(player):
                if isinstance(player.text, float):
                    tmp[table_header[index].text] = float(player.text)
                else:
                    tmp[table_header[index].text] = player.text.replace('-', ' - ')
            player_dict.append(tmp)

        # Write header to csv
        writer.writerow(tmp.keys())

        # Write data to csv
        for pl in player_dict:
            writer.writerow(pl.values())

    outfile.close()
