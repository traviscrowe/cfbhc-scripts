import util

class Data():
	def __init__(self, league, year, table):
		self.league = league
		self.year = year
		self.table = table
		self.tablePath = '//*[@id="mw-content-text"]/table[%s]' % (self.table)
		self.pageLink = "http://cfbhc.com/wiki/index.php?title=%s_%s_Season_Stats" % (self.year, self.league)
		self.cols = util.getColCount(table)