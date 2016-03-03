import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time


centerX = 20
centerY = 20
centerX2 = 400
centerY2 = 50 

class Swarm():

	def __init__(self):
		print ("Created this")

	def velocity(self):
		global centerX 
		centerX+=2
		global centerY 
		centerY+=2

class Window(QtGui.QMainWindow):

	test = Swarm()

	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(0, 0, 600, 600)
		self.setWindowTitle("Final Form")
		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.update)
		self.timer.start(20)
		self.show()

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

		#circle radius
		rad = 15
		global centerX
		global centerY
		#draw circle
		center = QPoint(centerX, centerY)

		paint.drawEllipse(center, rad, rad)

		# #add a new circle
		# center2 = QPoint(self.centerX2, self.centerY2)
		# paint.drawEllipse(center2, rad, rad)

		#move the circle every update
		self.test.velocity()
		paint.end()


def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())


if __name__ == "__main__":
	run()