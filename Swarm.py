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
		self.sizeBot = 3

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
				xPosBot = self.swarmCenterX + radiusSwarm * math.cos(thetaSwarm)
				yPosBot = self.swarmCenterY + radiusSwarm * math.sin(thetaSwarm)

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




if __name__=="__main__":
	print("its alive")