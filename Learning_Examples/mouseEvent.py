from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class DrawCircles(QWidget):
    center = QPoint(225, 125)
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(0, 0, 650, 550)
        self.setWindowTitle('Draw circles')
    def paintEvent(self, event):
        paint = QPainter()
        paint.begin(self)
        # optional
        paint.setRenderHint(QPainter.Antialiasing)
        # make a white drawing background
        paint.setBrush(Qt.white)
        paint.drawRect(event.rect())
        # for circle make the ellipse radii match
        radx = 20
        rady = 20
        # draw red circles
        paint.setPen(Qt.black)
        # center = QPoint(225, 125)
        placeholder = self.center
            # optionally fill each circle yellow
        paint.setBrush(Qt.green)
        paint.drawEllipse(placeholder, radx, rady)
        # paint.drawRect(10,10,20,20)
        paint.end()
    def mousePressEvent(self, QMouseEvent):
        tempCenter = str(QMouseEvent.pos())
        self.center = tempCenter[13:]
        update()




if __name__=="__main__":
    app = QApplication([])
    circles = DrawCircles()
    circles.show()
    app.exec_()