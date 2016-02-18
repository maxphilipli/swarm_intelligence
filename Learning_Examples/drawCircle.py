from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class DrawCircles(QWidget):
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
        paint.setPen(Qt.white)
        # for k in range(125, 220, 10):
        center = QPoint(xpos, 125)
            # optionally fill each circle yellow
        paint.setBrush(Qt.green)
        paint.drawEllipse(center, radx, rady)
        # paint.drawRect(10,10,20,20)
        paint.end()
    def mousePressEvent(self, QMouseEvent):
        print(QMouseEvent.pos())


if __name__=="__main__":
    global xpos
    xlist = [200, 125,250]
    app = QApplication([])
    circles = DrawCircles()

    # xpos = input("What's xpos: ")

    # if 'q' in xpos:
    #     sys.exit()
    for i in xlist:
        xpos = i
        circles.show()
        app.exec_()