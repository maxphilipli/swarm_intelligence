from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtOpenGL import QGLWidget
import sys
import random


class View(QGraphicsView,QObject):
    def __init__(self,parent=None):
        super(View,self).__init__(parent)
        #self.resize(600,300)
        self.viewport=QGLWidget()
        self.setViewport(self.viewport)
        self.setFixedSize(700,400)
        self.setAlignment(Qt.AlignTop|Qt.AlignLeft)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWindowTitle('Pong')
        # self.setWindowIcon(QIcon('pong.bmp'))

        self.setRenderHint(QPainter.Antialiasing)



    UPpress=pyqtSignal()
    DownPress=pyqtSignal()
    RightPress=pyqtSignal()
    LeftPress=pyqtSignal()

    def keyPressEvent(self,event):
        if event.key()==Qt.Key_Up:
            self.UPpress.emit()
        elif event.key()==Qt.Key_Down:
            self.DownPress.emit()
        elif event.key()==Qt.Key_Right:
            self.RightPress.emit()
        elif event.key()==Qt.Key_Left:
            self.LeftPress.emit()

        
        
    
class SceneAndView:
    def __init__(self):
        self.scene=QGraphicsScene()
        self.view=View()
        self.view.setScene(self.scene)
        self.scene.setBackgroundBrush(QColor(0,120,30))




class Paddle(QGraphicsRectItem):
    def __init__(self,maxHeight,parent=None):
        super(Paddle,self).__init__(parent)
        self.maxHeight=maxHeight-55

    def moveUp(self):
        #print self.y(),self.maxHeight
        if self.y()>0:
            self.setY(self.y()-10)

    def moveDown(self):
        #print self.y(),self.maxHeight
        if self.y()<self.maxHeight:
            self.setY(self.y()+10)

    def moveLeft(self):
        #print self.y(),self.maxHeight
        if self.x()>0:
            self.setX(self.x()-10)

    def moveRight(self):
        #print self.y(),self.maxHeight
        if self.x()<1000:
            self.setX(self.x()+10)


class PongGame:
    def __init__(self,parent=None):
        self.sceneView=SceneAndView()
        self.pen=QPen(Qt.green,5,Qt.SolidLine,Qt.FlatCap,Qt.RoundJoin)
        self.ballbrush=QBrush(Qt.red)
        self.paddlebrush=QBrush(Qt.black)
        

        self.paddleRight=Paddle(self.sceneView.view.height())
        self.paddleRight.setRect(0,0,10,50)

        self.paddleRight.setBrush(self.paddlebrush)
        self.sceneView.scene.addItem(self.paddleRight)
        self.sceneView.view.UPpress.connect(self.paddleRight.moveUp)
        self.sceneView.view.DownPress.connect(self.paddleRight.moveDown)
        self.sceneView.view.LeftPress.connect(self.paddleRight.moveLeft)
        self.sceneView.view.RightPress.connect(self.paddleRight.moveRight)
        
        
        self.timer=QTimer(self.sceneView.view)




if __name__=='__main__':
    app=QApplication(sys.argv)
    w=PongGame()
    w.sceneView.view.show()
    sys.exit(app.exec_())