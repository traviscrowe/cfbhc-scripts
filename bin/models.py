import json, collections

class Player():
	def __init__(self, cols = []):	
		self.position = cols[0]
		self.first_name = cols[1]
		self.last_name = cols[2]
		self.height = cols[3]
		self.weight = cols[4]
		self.year = cols[5]
		self.skill = cols[6]
		self.potential = cols[7]
		self.team = cols[8]
	def dump_JSON(self):
		return json.dumps(self.__dict__)
	def load_JSON(self):
		return json.loads(self.dump_JSON())

class Passer(Player):

	#Serialize into a passer object - expects 19 columns
	def __init__(self, cols = []):
		Player.__init__(self, cols[0:9])
		self.games = int(cols[9])
		self.completions = int(cols[10])
		self.attempts = int(cols[11])
		self.percentage = float(cols[12])
		self.yards = int(cols[13])
		self.tds = int(cols[14])
		self.ints = int(cols[15])
		self.rating = float(cols[16])
		self.ypa = float(cols[17])
		self.ypg = float(cols[18])

class Runner(Player):

	#Serialize into runner object - expects 17 columns
	def __init__(self, cols = []):
		Player.__init__(self, cols[0:9])
		self.games = int(cols[9])
		self.attempts = int(cols[10])
		self.yards = int(cols[11])
		self.tds = int(cols[12])
		self.fumbles = int(cols[13])
		self.hyg = int(cols[14])
		self.ypc = cols[15]
		self.ypg = cols[16]

class Reciever(Player):

	#Serialize into reciever object - expects 15 columns
	def __init__(self, cols = []):
		Player.__init__(self, cols[0:9])
		self.games = int(cols[9])
		self.catches = int(cols[10])
		self.yards = int(cols[11])
		self.tds = int(cols[12])
		self.ypc = float(cols[13])
		self.ypg = float(cols[14])

class Defender(Player):

	#Serialize into defender object - expects 18 columns
	def __init__(self, cols = []):
		Player.__init__(self, cols[0:9])
		self.games = int(cols[9])
		self.tackles = int(cols[10])
		self.ints = int(cols[11])
		self.sacks = float(cols[12])
		self.ff = int(cols[13])
		self.fr = int(cols[14])
		self.blocks = int(cols[15])
		self.tds = int(cols[16])
		self.safeties = int(cols[17])

class Kicker(Player):

	#Serialize into kicker object - expects 16 columns
	def __init__(self, cols = []):
		Player.__init__(self, cols[0:9])
		self.attempts = int(cols[8])
		self.missed = int(cols[9])
		self.under_twenty = int(cols[11])
		self.twenties = int(cols[12])
		self.thirties = int(cols[13])
		self.fourties = int(cols[14])
		self.fifties = int(cols[15])

class Returner(Player):

	#Serialize into kick/punt returner object - expects 10 columns
	def __init__(self, cols = []):
		Player.__init__(self, cols[0:9])
		self.kickoff_tds = int(cols[9])
		self.punt_tds = int(cols[10])