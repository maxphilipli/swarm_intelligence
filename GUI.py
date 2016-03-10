import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time


#-----------------------------------------------------------#
#GUI class definition
class Window(QtGui.QMainWindow):

	#---------------------------------------------#
	#define class variables
	msPtX = 20
	msPtY = 20
	centerX = 20
	centerY = 20

	#---------------------------------------------#
	#define what to do on initialization
	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(0, 0, 500, 500)
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
		if self.msPtX > self.centerX:
			self.centerX += 3
		if self.msPtY > self.centerY:
			self.centerY += 3
		if self.msPtX < self.centerX:
			self.centerX -= 3
		if self.msPtY < self.centerY:
			self.centerY -= 3		

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
		rad = 15
		center = QPoint(self.centerX, self.centerY)
		paint.drawEllipse(center, rad, rad)

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