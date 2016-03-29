import math


class Bot():

	def __init__(self, xPos, yPos, velocity, theta, size):
		self.xPos = xPos
		self.yPos = yPos
		self.velocity = velocity
		self.theta = theta
		self.size = size
		self.sight = 10
		self.newX = 0
		self.newY = 0

	


	def calcPos(self):
		# Calculates the position based on velocity and theta
		self.newX = self.xPos + self.velocity*math.cos(self.theta)
		self.newY = self.yPos + self.velocity*math.sin(self.theta)


	def distance(self, x, y, x2, y2):
		return math.sqrt((x-x2)*(x-x2) + (y-y2)*(y-y2))

	def calcVelocity(self, x, y):
		# Calculates the velocity for the bot
		factor = 1
		dist = self.distance(self.xPos, self.yPos, x, y)
		# print (dist)
		self.velocity = factor * dist
		if self.velocity >= 4:
			self.velocity = 4
		if dist <= 5:
			self.velocity = 0
		self.theta = math.atan2(y - self.yPos, x - self.xPos)

	def move(self, x, y, bList):
		# Function to simply movement function call in GUI
		self.calcVelocity(x, y)
		self.calcPos()
		if self.compare(bList):
			self.xPos = self.newX
			self.yPos = self.newY

	def compare(self, bList):
		for element in bList:
			if (element.xPos and element.yPos) == (self.xPos and self.yPos):
				pass
			elif self.distance(element.xPos, element.yPos, self.newX, self.newY) < (element.size + self.size):
				return False
		return True






if __name__=="__main__":
	a = Bot(0,0,0,math.pi, 1)

	print("xpos = ", a.xPos)
	print("ypos = ", a.yPos)
	print("theta = ", a.theta)
	print("sight = ", round(a.sight))

	a.move(1, 1)

	print ("")
	print("xpos = ", a.xPos)
	print("ypos = ", a.yPos)
	print("theta = ", a.theta)
	print("sight = ", round(a.sight))

	# for  i in range(0, 10):
	# 	a.calcVelocity()
	# 	a.calcPos()

	# 	print("xpos = ", a.xPos)
	# 	print("ypos = ", a.yPos)
	# 	print("vel = ", a.velocity)