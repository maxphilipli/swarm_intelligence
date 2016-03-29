import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time
import math
import Bot
import Swarm


#-----------------------------------------------------------#
#GUI class definition
class Window(QtGui.QMainWindow):

	#---------------------------------------------#
	#define class variables
	msPtX = 20
	msPtY = 20

	swarm = Swarm.Swarm(100, 50)
	#---------------------------------------------#
	#define what to do on initialization
	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(200, 200, 500, 500)
		self.setWindowTitle("Final Form")
		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.update)
		self.timer.start(20)
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
		for element in self.swarm.botList:
			element.move(self.msPtX, self.msPtY)


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

		# self.bot.calcVelocity()
		# self.bot.calcPos()

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