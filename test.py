from PyQt4.QtCore import *
from PyQt4.QtGui import *

class DrawCircles(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(300, 300, 350, 350)
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
        radx = 100
        rady = 100
        # draw red circles
        paint.setPen(Qt.blue)
        # for k in range(125, 220, 10):
        center = QPoint(225, 125)
            # optionally fill each circle yellow
        paint.setBrush(Qt.green)
        paint.drawEllipse(center, radx, rady)
        paint.end()

if __name__=="__main__":
    app = QApplication([])
    circles = DrawCircles()
    circles.show()
    app.exec_()