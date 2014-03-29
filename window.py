# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Sat Mar 29 12:41:19 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

"""
import sys
from PyQt4.QtCore import *
from PyQt4 import QtGui

class SomeScene(QtGui.QGraphicsScene):
    def __init__(self, parent = None):
        QtGui.QGraphicsScene.__init__(self, parent)

        pixmap = QtGui.QPixmap("upload.png")
        item = QtGui.QGraphicsPixmapItem(pixmap)
        self.addItem(item)


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)

        self.scene = SomeScene()
        view = QtGui.QGraphicsView(self.scene)

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(view)

        mainWidget = QtGui.QWidget()
        mainWidget.setLayout(hbox)

        self.setCentralWidget(mainWidget)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
"""

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from PySide import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ImageView(QGraphicsView):
    def __init__(self, parent=None, origPixmap=None):
        super(ImageView, self).__init__(parent)
        self.origPixmap = origPixmap
        QMetaObject.connectSlotsByName(self)

    def resizeEvent(self, event):
        size = event.size()
        item =  self.items()[0]

        # using current pixmap after n-resizes would get really blurry image
        #pixmap = item.pixmap()
        pixmap = self.origPixmap

        pixmap = pixmap.scaled(size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.centerOn(1.0, 1.0)
        item.setPixmap(pixmap)


app = QApplication(sys.argv)

Dialog.setObjectName("Dialog")
Dialog.resize(747, 482)

pic = QPixmap("upload.png")
grview = ImageView(origPixmap=pic)

scene = QGraphicsScene()
scene.addPixmap(pic)
scene.resize(512, 512)

grview.setScene(scene)
grview.show()

sys.exit(app.exec_())



"""
from PySide import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(747, 482)
        self.graphicsView = QtGui.QGraphicsView(Dialog)
        self.graphicsView.setGeometry(QtCore.QRect(70, 30, 621, 401))
        self.graphicsView.setObjectName("graphicsView")


        self.graphicsView.addPixmap(QPixmap("upload.png"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.graphicsView.show()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))

if __name__ == '__main__':
    window = Ui_Dialog()
    window.setupUi()
"""