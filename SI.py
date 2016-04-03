import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time
import math
import Bot
import Swarm
import Obstacle
import random


#-----------------------------------------------------------#
#GUI class definition
class Window(QtGui.QMainWindow):

	#---------------------------------------------#
	#define class variables
	msPtX = 20
	msPtY = 20

	swarm = Swarm.Swarm(100, 50)

	# obs = Obstacle.Obstacle(75, 500, 300)
	# obs2 = Obstacle.Obstacle(40, 100, 450)
	# obs3 = Obstacle.Obstacle(40, 300, 450)
	# obs4 = Obstacle.Obstacle(40, 500, 450)
	# obs5 = Obstacle.Obstacle(40, 100, 250)
	# obs6 = Obstacle.Obstacle(40, 300, 250)
	# obs7 = Obstacle.Obstacle(40, 500, 250)
	# obsList = [obs, obs2, obs3, obs4, obs5, obs6, obs7]
	obsList = []
	for i in range(0,100):
		x = random.uniform(50, 950)
		y = random.uniform(50, 950)
		obsList.append(Obstacle.Obstacle(20,x,y))




	#---------------------------------------------#
	#define what to do on initialization
	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(100, 200, 1000, 1000)
		self.setWindowTitle("Final Form")
		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.update)
		self.timer.start(2)
		self.show()

	#---------------------------------------------#
	#grab coordinates of mouse click
	def mousePressEvent(self, QMouseEvent):
		mousePoint = (str(QMouseEvent.pos())[20:])
		mousePoint = mousePoint.rsplit(", ")
		msPtX = mousePoint[0]
		noEndP = mousePoint[1].rsplit(")")
		msPtY = noEndP[0]
		self.msPtX = int(msPtX)
		self.msPtY = int(msPtY)

	#---------------------------------------------#
	#movement to mouse coordinates after mouse click
	def moveToMouse(self):
		self.swarm.updateBotList(self.msPtX, self.msPtY)
		for element in self.swarm.botList:
			element.move(self.msPtX, self.msPtY, self.swarm.botList, self.obsList)


	#---------------------------------------------#
	#paint event being looped to simulate animation
	def paintEvent(self, event):
		paint = QPainter()
		paint.begin(self)
		paint.setRenderHint(QPainter.Antialiasing)
		#set background
		paint.setBrush(Qt.white)
		paint.drawRect(event.rect())
		#set circle
		paint.setPen(Qt.black)
		paint.setBrush(Qt.green)
		#draw circle
		# rad = 15
		# center = QPoint(self.bot.xPos, self.bot.yPos)
		# paint.drawEllipse(center, rad, rad)

		#draw a swarm of bots
		for element in self.swarm.botList:
			center = QPoint(element.xPos, element.yPos)
			paint.drawEllipse(center, element.size, element.size)

		#create object to draw
		paint.setBrush(Qt.blue)
		for element in self.obsList:
			obsCenter = QPoint(element.xPos, element.yPos)
			paint.drawEllipse(obsCenter, element.size, element.size)

		self.moveToMouse()

		paint.end()




#-----------------------------------------------------------#
def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())


#-----------------------------------------------------------#
if __name__ == "__main__":
	run()