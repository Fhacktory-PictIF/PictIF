# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pictInterface.ui'
#
# Created: Sat Mar 29 12:47:38 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PySide import QtCore, QtGui

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeModule = QtGui.QTreeWidget(self.centralwidget)
        self.treeModule.setGeometry(QtCore.QRect(0, 220, 231, 341))
        self.treeModule.setObjectName("listeModule")
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(240, 90, 551, 461))
        self.graphicsView.setObjectName("graphicsView")
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



    mySW.show()
    sys.exit(app.exec_())