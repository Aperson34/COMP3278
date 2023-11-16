# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from sidebar import Sidebar

class MenuBar(object):
    
    def showSideBar(self,MainWindow):
        MainWindow.HLayoutWidget.setGeometry(QtCore.QRect(0, 0, 709, 1080))
        ui = Sidebar()
        ui.setupUi(MainWindow)
        MainWindow.HLayout.addWidget(ui.frame)
        print('clicked')

    def setupUi(self, MainWindow):
        self.frame = QtWidgets.QFrame()
        self.frame.setFixedHeight(128)
        self.frame.setFixedWidth(1920)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("background-color: rgb(206,194,204);")
        
        self.menuicon = QtWidgets.QPushButton(self.frame)
        self.menuicon.setIcon(QtGui.QIcon("GUI/menu.svg"))
        self.menuicon.setGeometry(QtCore.QRect(0, 0, 75, 25))
        self.menuicon.setObjectName("menuicon")
        self.menuicon.clicked.connect(lambda:self.showSideBar(MainWindow))


        self.menuusername = QtWidgets.QLabel(self.frame)
        self.menuusername.setStyleSheet("color: rgb(255, 255, 255)")
        self.menuusername.setObjectName("menuusername")
        self.menuusername.setGeometry(QtCore.QRect(700, 0, 75, 25))

        # self.menubar.addAction(self.menuicon.menuAction())
        # self.menubar.addAction(self.menuusername.menuAction())
        MainWindow.gridLayout.addWidget(self.frame,0,0,1,3)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.menuusername.setText(_translate("Form", "UserName"))