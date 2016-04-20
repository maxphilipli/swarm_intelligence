import math
import random
import Bot


class Swarm():

	def __init__(self, numberBots, startSize):
		self.numberBots = numberBots
		self.startSize = startSize
		self.botList = []
		self.swarmStartX = 200
		self.swarmStartY = 200
		self.sizeBot = 3
		self.swarmCenterX = 0
		self.swarmCenterY = 0

		for i in range(0,numberBots):
			overlap = True
			counter = 0
			while overlap: 
				counter += 1
				if counter > 1000:
					print('You Fucked up! Not enought space')
					self.botList = []
					return
				# create random position of bot within defined radius
				radiusSwarm = random.uniform(0, self.startSize)
				thetaSwarm = random.uniform(0, 2*math.pi)
				
				# define Bot initial variables
				xPosBot = self.swarmStartX + radiusSwarm * math.cos(thetaSwarm)
				yPosBot = self.swarmStartY + radiusSwarm * math.sin(thetaSwarm)

				if i > 0:
					for element in self.botList:
						dist = element.distance(xPosBot,yPosBot, element.xPos, element.yPos)
						if dist > 2*self.sizeBot:
							overlap = False
						else:
							overlap = True
							break

				else:
					overlap = False


			thetaBot = 0
			velocityBot = 0

			# create Bot and add to list
			newBot = Bot.Bot(xPosBot,yPosBot, velocityBot, thetaBot, self.sizeBot)
			self.botList.append(newBot)
			# print('made many bots',i)

	def updateBotList(self, targX, targY):
		for element in self.botList:
			element.distToTargFunc(targX, targY)
		self.botList = sorted(self.botList, key=lambda bot: bot.distToTarg)

	def findCenter(self):
		self.swarmCenterX = 0
		self.swarmCenterY = 0
		for element in self.botList:
			self.swarmCenterX += element.xPos
			self.swarmCenterY += element.yPos

		self.swarmCenterX /= self.numberBots
		self.swarmCenterY /= self.numberBots








if __name__=="__main__":
	print("its alive")