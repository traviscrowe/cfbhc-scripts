# cfbhc-scripts

Simulation football stat data manipulation scripts for the fine folks at cfbhc.com

###About

These are scripts meant to parse player data located at the cfbhc.com wiki (an example would be cfbhc.com/wiki/2017_NFLHC_Season_Stats), and return each row as JSON for consumption by other systems

###How to Use

~~Right now (7/13/2015), only the files in 2014_2017_nflhc are stable enough to run, but generally here's how it works:~~

~~As of 7/14/2015, both sets of scripts are fully-functional against the existing wiki tables:~~

As of 6/3/2016, CFBHC and NFLHC parsing works for all seasons 2014-2018

1. Open **bin/run.py**
2. Notice the three variables LEAGUE_SELECTED, YEAR_SELECTED, TABLE_SELECTED - these are the primary configurations to parse the tables.
  * LEAGUE_SELECTED can be "NFLHC" or "CFBHC"(use LEAGUE[0] or LEAGUE[1])
  * YEAR_SELECTED can be 2014 - 2018 (the two years that use the table format defined for NFLHC)
  * TABLE_SELECTED can be any of the following:
    * 0: Passing Stats
    * 1: Rushing Stats
    * 2: Receiving Stats
    * 3: Defensive Stats
    * 4: Kicking Stats
    * 5: Returning Stats (n/a in 2014)
    * 6: Team Stats (not yet implemented)
3. Once configurations are set, run the script and enjoy!

###Future Development

~~I plan to add support for 2015/2016 in NFLHC and each year from 2014-2017 in CFBHC at the very least.~~ (DONE)

~~Export to CSV is pretty high on the list as well.~~ (DONE)

There's also the potential to turn these scripts into a full-blown API for consumption.

Google Sheets integration
