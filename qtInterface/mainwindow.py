# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pictInterface.ui'
#
# Created: Sat Mar 29 12:47:38 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PySide import QtCore, QtGui

class UIBlock(QtGui.QGraphicsObject):

    def __init__(self, filepath):
        super(UIBlock, self).__init__()
        #self.pixmap = QtGui.QPixmap.grabWidget(filepath)
        pixmap = QtGui.QPixmap(filepath)

        # below makes the pixmap half transparent
        painter = QtGui.QPainter(pixmap)
        painter.setCompositionMode(painter.CompositionMode_DestinationIn)
        painter.fillRect(pixmap.rect(), QtGui.QColor(0, 0, 0, 127))
        painter.end()

    def dragEnterEvent(self, e):
        print('drag enter event')
        e.accept()

    def dragLeageEvent(self, e):
        print('drag lave event')
        e.accept()

    def dropEvent(self, e):
        print('drop event')
        e.accept()


    def mouseMoveEvent(self, e):
        print "mouse moved event"
        if e.buttons() != QtCore.Qt.LeftButton:
            return

        # write the relative cursor position to mime data
        mimeData = QtCore.QMimeData()
        #mimeData.setText('%d,%d' % (e.x(), e.y()))

        # make a QDrag
        drag = QtGui.QDrag(self)
        # put our MimeData
        drag.setMimeData(mimeData)
        # set its Pixmap
        drag.setPixmap(self.pixmap)
        # shift the Pixmap so that it coincides with the cursor position
        drag.setHotSpot(e.pos())

        # start the drag operation
        # exec_ will return the accepted action from dropEvent
        if drag.exec_(QtCore.Qt.CopyAction | QtCore.Qt.MoveAction) == QtCore.Qt.MoveAction:
            print 'moved'
        else:
            print 'copied'


    def mousePressEvent(self, e):
        QtGui.QPushButton.mousePressEvent(self, e)
        if e.button() == QtCore.Qt.LeftButton:
            print 'Mouse pressed button'

class UIParseBlock(UIBlock):
    def __init__(self):
        super(UIParseBlock, self).__init__("../img/upload.png")


class BlocksGraphicsView(QtGui.QGraphicsView):
    def __init__(self, parent=None):
        super(BlocksGraphicsView, self).__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        print('graphics view drag enter')
        e.accept()


    def dropEvent(self, e):
        # get the relative position from the mime data
        print('graphics view drop')
        mime = e.mimeData().text()
        x, y = map(int, mime.split(','))
        e.source().move(e.pos()-QtCore.QPoint(x, y))
        # set the drop action as Move
        e.setDropAction(QtCore.Qt.MoveAction)
        #event.acceptProposedAction()
        e.accept()

    def mousePressEvent(self, ev):
        print "mouse pressed 2"
        if ev.button() == QtCore.Qt.LeftButton:
            pass #Useful to create links


class Ui_MainWindow(QtGui.QMainWindow):
    blockScene = None
    blocks = []

    def addBlockPresentation(self, block):
        self.blocks.append(block)
        #self.blockScene.addPixmap(block)
        self.blockScene.addItem(block)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeModule = QtGui.QTreeWidget(self.centralwidget)
        self.treeModule.setGeometry(QtCore.QRect(0, 220, 231, 341))
        self.treeModule.setObjectName("listeModule")
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.listeModule = QtGui.QListView(self.centralwidget)
        self.listeModule.setGeometry(QtCore.QRect(0, 220, 231, 341))
        self.listeModule.setObjectName("listeModule")
        self.graphicsView = BlocksGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(240, 90, 551, 461))
        self.graphicsView.setObjectName("graphicsView")

        self.blockScene = QtGui.QGraphicsScene()
        self.blockScene.setSceneRect(self.graphicsView.rect())
        self.graphicsView.setScene(self.blockScene)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def init_user(self) :
        #create actions to be put in file menu

        #action to open project
        openProjectAction = QtGui.QAction( '&Open project', self)
        openProjectAction.setShortcut('Ctrl+O')
        openProjectAction.setStatusTip('Open project')


        #action to exit
        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)



        self.fileMenu = self.menubar.addMenu('&File')
        self.settingsMenu = self.menubar.addMenu('&Settings')
        self.helpMenu = self.menubar.addMenu('&Help')
        self.toolsMenu = self.menubar.addMenu('&Tools')

        self.fileMenu.addAction(exitAction)
        self.fileMenu.addAction(openProjectAction)


        #self.treeWidget = QtGui.QTreeWidget()
        self.treeModule.setColumnCount(1)
        items = []
        for i in range(10):
            item = QtGui.QTreeWidgetItem(None,  [str(i)])
            item.setText(0,"pihjoi")
            print(item.text(0))
            items.append(item)

        drag = QtGui.QDrag(self.treeModule)
        drag.setHotSpot(QtCore.QPoint(drag.pixmap().width()/2,
                       drag.pixmap().height()))

        QtGui.QDrag(self.treeModule)
        print(drag.source())

        self.treeModule.insertTopLevelItems(1, items)




    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))

class ControlMainWindow(QtGui.QMainWindow):
  def __init__(self, parent=None):
    super(ControlMainWindow, self).__init__(parent)
    self.ui =  Ui_MainWindow()
    self.ui.setupUi(self)
    self.ui.init_user()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    #mySW.ui.addBlockPresentation(UIParseBlock())
    mySW.show()
    sys.exit(app.exec_())