#Help!

###About

These are scripts meant to parse player data located at the cfbhc.com wiki (an example would be cfbhc.com/wiki/2017_NFLHC_Season_Stats), and return each row as JSON for consumption by other systems

###How to Use

Right now (7/13/2015), only the files in 2014_2017_nflhc are stable enough to run, but generally here's how it works:

1. Open 2014_2017_nflhc_player_stats.py
2. Notice the three variables LEAGUE_SELECTED, YEAR_SELECTED, TABLE_SELECTED - these are the primary configurations to parse the tables.
  * LEAGUE_SELECTED can be "NFLHC" (use LEAGUE[0] as is set by default)
  * YEAR_SELECTED can be 2014 or 2017 (the two years that use the table format defined for NFLHC)
  * TABLE_SELECTED can be any of the following:
    * 0: Passing Stats
    * 1: Rushing Stats
    * 2: Recieving Stats
    * 3: Defensive Stats
    * 4: Kicking Stats
    * 5: Returning Stats (n/a in 2014)
    * 6: Team Stats (not yet implemented)
3. Once configurations are set, run 2014_2017_nflhc_player_stats.py and enjoy!

###Future Development

I plan to add support for 2015/2016 in NFLHC and each year from 2014-2017 in CFBHC at the very least. There's also the potential to turn these scripts into a full-blown API for consumption.