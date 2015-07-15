import util

class Data():
	def __init__(self, league, year, table):
		self.league = league
		self.year = year
		if(league == "CFBHC" and (year == "2015" or year == "2016")): self.table = table + 1
		else: self.table = table
		self.table_path = '//*[@id="mw-content-text"]/table[%s]' % (self.table) #account for team stats 
		self.page_link = "http://cfbhc.com/wiki/index.php?title=%s_%s_Season_Stats" % (self.year, self.league)
		self.cols = util.get_col_count(table)