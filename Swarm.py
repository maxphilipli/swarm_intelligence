import math
import random
import Bot


class Swarm():

	def __init__(self, numberBots, startSize):
		self.numberBots = numberBots
		self.startSize = startSize
		self.botList = []
		self.swarmCenterX = 200
		self.swarmCenterY = 200

		for i in range(0,numberBots):
			# create random position of bot within defined radius
			radiusSwarm = random.uniform(0, self.startSize)
			thetaSwarm = random.uniform(0, 2*math.pi)

			# define Bot initial variables
			xPosBot = self.swarmCenterX + radiusSwarm * math.cos(thetaSwarm)
			yPosBot = self.swarmCenterY + radiusSwarm * math.sin(thetaSwarm)
			thetaBot = 0
			velocityBot = 0

			# create Bot and add to list
			newBot = Bot.Bot(xPosBot,yPosBot, velocityBot, thetaBot)
			self.botList.append(newBot)





if __name__=="__main__":
	print("its alive")
	# a = Bot(0,0,0,math.pi/4)

	# print("xpos = ", a.xPos)
	# print("ypos = ", a.yPos)
	# print("theta = ", a.theta)
	# print("sight = ", round(a.sight))

	# a.calcVelocity()
	# a.calcPos()

	# print("xpos = ", a.xPos)
	# print("ypos = ", a.yPos)
	# print("vel = ", a.velocity)

	# a.calcVelocity()
	# a.calcPos()

	# print("xpos = ", a.xPos)
	# print("ypos = ", a.yPos)
	# print("vel = ", a.velocity)