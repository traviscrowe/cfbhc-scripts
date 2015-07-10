import json

POSITIONS = [('Passing', 19), ('Rushing', 17), ('Recieving', 15), ('Defensive', 18)]

class Passer():

	#serialize into a passer object
	def __init__(self, cols = []):
		self.position = cols[0]
		self.firstName = cols[1]
		self.lastName = cols[2]
		self.height = cols[3]
		self.weight = int(cols[4])
		self.year = cols[5]
		self.skill = int(cols[6])
		self.team = cols[7]
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
	def to_JSON(self):
		return json.dumps(self.__dict__)