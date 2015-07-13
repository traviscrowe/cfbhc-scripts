import json
import collections

class Player():
	def __init__(self, cols = []):	
		self.position = cols[0]
		self.first_name = cols[1]
		self.last_name = cols[2]
		self.height = cols[3]
		self.weight = int(cols[4])
		self.year = cols[5]
		self.skill = int(cols[6])
		self.team = cols[7]
	def to_JSON(self):
		return json.dumps(self.__dict__)

class Passer(Player):

	#Serialize into a passer object - expects 20 columns
	def __init__(self, cols = []):
		Player.__init__(self, cols[0:8])
		self.games = int(cols[8])
		self.completions = int(cols[9])
		self.attempts = int(cols[10])
		self.percentage = float(cols[11])
		self.yards = int(cols[12])
		self.tds = int(cols[13])
		self.ints = int(cols[14])
		self.rating = float(cols[15])
		self.ypa = float(cols[16])
		self.ypg = float(cols[17])
		self.tdpct = float(cols[18])
		self.intpct = float(cols[19])

class Runner(Player):

	#Serialize into runner object - expects 16 columns
	def __init__(self, cols = []):
		Player.__init__(self, cols[0:8])
		self.games = int(cols[8])
		self.attempts = int(cols[9])
		self.yards = int(cols[10])
		self.tds = int(cols[11])
		self.fumbles = int(cols[12])
		self.hyg = int(cols[13])
		self.ypc = float[cols[14]]
		self.ypg = float[cols[15]]

class Reciever(Player):

	#Serialize into reciever object - expects 15 columns
	def __init__(self, cols = []):
		Player.__init__(self, cols[0:8])
		self.games = int(cols[8])
		self.catches = int(cols[9])
		self.yards = int(cols[10])
		self.tds = int(cols[11])
		self.fumbles = int(cols[12])
		self.ypc = float(cols[13])
		self.ypg = float(cols[14])

class Defender(Player):

	#Serialize into defender object - expects 17 columns
	def __init__(self, cols = []):
		Player.__init__(self, cols[0:8])
		self.games = int(cols[8])
		self.tackles = int(cols[9])
		self.ints = int(cols[10])
		self.sacks = float(cols[11])
		self.ff = int(cols[12])
		self.fr = int(cols[13])
		self.blocks = int(cols[14])
		self.tds = int(cols[15])
		self.safeties = int(cols[16])

class Kicker(Player):

	#Serialize into kicker object - expects 16 columns
	def __init__(self, cols = []):
		Player.__init__(self, cols[0:8])
		self.attempts = int(cols[8])
		self.missed = int(cols[9])
		self.percentage = float(cols[10])
		self.under_twenty = int(cols[11])
		self.twenties = int(cols[12])
		self.thirties = int(cols[13])
		self.fourties = int(cols[14])
		self.fifties = int(cols[15])

class Returner(Player):

	#Serialize into kick/punt returner object - expects 10 columns
	def __init__(self, cols = []):
		Player.__init__(self, cols[0:8])
		self.kickoff_tds = int(cols[8])
		self.punt_tds = int(cols[9])