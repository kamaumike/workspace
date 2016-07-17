class Horse(object):
	"""Horse represents a Horse"""

	species = "Thorough Bred"
	def __init__(self, color, weight, wild =  False):
		self.color = color
		self.weight = weight
		self.wild = wild

	def __repr__(self):
		return "%s horse weighing %f and wild status is %b" % (self.color, self.weight, self.wild)
 
	def make_sound(self):
		print "neighhhh"

	def movement(self):
		return "walk"	


class RaceHorse(Horse):
	"""A faster horse that inherits from Horse"""
	def movement(self):
		return "run"
	def movement_slow(self):
		return super(Horse,self).movement()
	def __repr__(self):
		return "%s race horse weighing %f and wild status is %b" % (self.color, self.weight, self.wild)	


horse3 = RaceHorse("white", 200)		

print horse3.movement_slow()
print horse3.movement()		
	
			
		