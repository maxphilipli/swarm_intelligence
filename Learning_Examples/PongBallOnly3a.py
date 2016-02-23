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
        self.setWindowIcon(QIcon('pong.bmp'))
        self.setRenderHint(QPainter.Antialiasing)
     
        
        
    
class SceneAndView:
    def __init__(self):
        self.scene=QGraphicsScene()
        self.view=View()
        self.view.setScene(self.scene)
        self.scene.setBackgroundBrush(QColor(0,120,30))


class Ball(QGraphicsEllipseItem):
    def __init__(self,parent=None):
        super(Ball,self).__init__(parent)
        self.vel=[0,0]
        self.radius=16

    def reflectX(self):
        self.vel[0]=-self.vel[0]
        if self.vel[0]<0:
            self.vel[0]-=00.5
        else:
            self.vel[0]+=0.5
        self.setX(self.x()+self.vel[0])
        
    def reflectY(self):
        self.vel[1]=-self.vel[1]
        self.setY(self.y()+self.vel[1])


    def move(self):
        self.setX(self.x()+self.vel[0])
        self.setY(self.y()+self.vel[1])
        



class PongGame:
    def __init__(self,parent=None):
        self.sceneView=SceneAndView()
        self.pen=QPen(Qt.green,5,Qt.SolidLine,Qt.FlatCap,Qt.RoundJoin)
        self.ballbrush=QBrush(Qt.red)
       
        
        self.ball=Ball()
        self.ball.setBrush(self.ballbrush)
        self.ball.setRect((self.sceneView.view.size().width()-15)/2,self.sceneView.view.height(),self.ball.radius,self.ball.radius)
        self.boundary=[self.sceneView.view.width(),self.sceneView.view.height()]
        
        self.sceneView.scene.addItem(self.ball)
        
        self.scoreText=QGraphicsTextItem()
        
        self.sceneView.scene.addItem(self.scoreText)

        self.scoreText.setPos(self.boundary[0]/2-self.scoreText.boundingRect().width()*.85,self.boundary[1]/2)
        self.scoreText.setFont(QFont('Arial',15))
        
        self.timer=QTimer(self.sceneView.view)
        self.timer.timeout.connect(self.ballMove)
        self.reset()


        
    def reset(self):
        self.serve(random.choice([0,1]))

    def serve(self,leftSide):
        self.ball.setPos(0,0)

        if leftSide:
            self.ball.vel=[-10,random.choice([-3,-2,-1,1,2,3])]
        else:
            self.ball.vel=[10,random.choice([-3,-2,-1,3,2,1])]
        self.timer.start(32)

    def ballMove(self):
        if self.ballHitsBoundary():
            self.ball.reflectY()
        elif self.ballHitsWalls():
            self.ball.reflectX()            

        else:
            self.ball.move()

            
    def ballHitsBoundary(self):
        if self.ball.y()<-self.boundary[1]/2+15 or self.ball.y()>self.boundary[1]/2-15:
            return True
        pass

    def ballHitsWalls(self):
        z = self.sceneView.scene.collidingItems(self.ball)
        if self.ball.x() < 0 or self.ball.x() > 670:
            return True
        pass



if __name__=='__main__':
    app=QApplication(sys.argv)
    w=PongGame()
    w.sceneView.view.show()
    sys.exit(app.exec_())