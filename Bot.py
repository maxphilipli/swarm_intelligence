import math


class Bot():

	def __init__(self, xPos, yPos, velocity, theta):
		self.xPos = xPos
		self.yPos = yPos
		self.velocity = velocity
		self.theta = theta
		self.size = 1
		self.sight = 10

	

	def calcPos(self):
		# Calculates the position based on velocity and theta
		print("calcPos")
		self.xPos = self.xPos + self.velocity*math.cos(self.theta)
		self.yPos = self.yPos + self.velocity*math.sin(self.theta)




	def calcVelocity(self):
		# Calculates the velocity for the bot
		print("calcVelocity")
		self.velocity  += 1
		

	def calcTheta(self):
		#Calculates the theta for the bot
		print("calcTheta")




if __name__=="__main__":
	a = Bot(0,0,0,math.pi/4)

	print("xpos = ", a.xPos)
	print("ypos = ", a.yPos)
	print("theta = ", a.theta)
	print("sight = ", round(a.sight))

	for  i in range(0, 10):
		a.calcVelocity()
		a.calcPos()
		
		print("xpos = ", a.xPos)
		print("ypos = ", a.yPos)
		print("vel = ", a.velocity)