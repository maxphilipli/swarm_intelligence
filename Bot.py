import math
import random
import Obstacle

class Bot():

	def __init__(self, xPos, yPos, velocity, theta, size):
		self.xPos = xPos
		self.yPos = yPos
		self.velocity = velocity
		self.theta = theta
		self.size = size        #size is radius
		self.sight = 10
		self.newX = 0
		self.newY = 0
		self.distToTarg = 0
		self.randVar = random.uniform(0, 1)

	

	def calcPos(self):
		# Calculates the position based on velocity and theta
		self.newX = self.xPos + self.velocity*math.cos(self.theta)
		self.newY = self.yPos + self.velocity*math.sin(self.theta)



	def distance(self, x, y, x2, y2):
		return math.sqrt((x-x2)*(x-x2) + (y-y2)*(y-y2))

	def calcVelocity(self, x, y, bList, obsList):
		# Calculates the velocity for the bot
		factor = .05
		dist = self.distance(self.xPos, self.yPos, x, y)
		self.velocity = factor * dist
		if self.velocity >= 8:
			self.velocity = 8
		if dist <= 5:
			self.velocity = 0

		#attraction force for target and repulsion force for bots
		targWeight = 300
		targDX = ((x - self.xPos)/dist) * targWeight
		targDY = ((y - self.yPos)/dist) * targWeight

		for element in bList:
			bDist = self.distance(self.xPos, self.yPos, element.xPos, element.yPos)
			dmax = 250
			dmin = 20
			botWeight = -1/(dmax - dmin) * bDist + dmax/(dmax - dmin)
			if botWeight > 1:
				botWeight = 1
			elif botWeight < 0:
				botWeight = 0
			if bDist != 0:
				pass
				targDX += -((element.xPos - self.xPos)/bDist)*botWeight
				targDY += -((element.yPos - self.yPos)/bDist)*botWeight



		for obs in obsList:

			obsDist = self.distance(self.xPos, self.yPos, obs.xPos, obs.yPos)
			multFactor = 5000

			obsDX1 = obs.xPos - self.xPos
			obsDY1 = obs.yPos - self.yPos

			if (targDX * obsDY1 - targDY * obsDX1) > 0:
				self.randVar = 0
			else:
				self.randVar = 1





			if self.randVar < 0.5:
				obsDX2 = obsDY1
				obsDY2 = -obsDX1
			else:
				obsDX2 = -obsDY1
				obsDY2 = obsDX1
			
			if (obsDist - (obs.size + self.size)) <= 0:
				obsWeight = 100000 * multFactor
			else:
				obsWeight = multFactor/(obsDist - (obs.size + self.size))

			targDX += (obsDX2 / obsDist) * obsWeight
			targDY += (obsDY2 / obsDist) * obsWeight


		self.theta = math.atan2(targDY, targDX) + random.gauss(0, math.pi/6)

	def move(self, x, y, bList, obsList):
		# Function to simply movement function call in GUI
		self.calcVelocity(x, y, bList, obsList)
		self.calcPos()
		if self.collisionChecker(bList, obsList):
			self.xPos = self.newX
			self.yPos = self.newY

	def collisionChecker(self, bList, obsList):
		for element in bList + obsList:
			if (element.xPos and element.yPos) == (self.xPos and self.yPos):
				pass
			elif self.distance(element.xPos, element.yPos, self.newX, self.newY) < (element.size + self.size):
				return False
		return True

	def distToTargFunc(self, targX, targY):
		self.distToTarg = ((self.xPos-targX)*(self.xPos-targX) + (self.yPos-targY)*(self.yPos-targY))










if __name__=="__main__":
	a = Bot(0,0,0,math.pi, 1)

	# print("xpos = ", a.xPos)
	# print("ypos = ", a.yPos)
	# print("theta = ", a.theta)
	# print("sight = ", round(a.sight))

	# a.move(1, 1)

	# print ("")
	# print("xpos = ", a.xPos)
	# print("ypos = ", a.yPos)
	# print("theta = ", a.theta)
	# print("sight = ", round(a.sight))