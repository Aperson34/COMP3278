# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\course_info.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import time
#from sql
class WelMsg(object):
    
    def removeMsg(self):
        _translate = QtCore.QCoreApplication.translate
        self.textBrowser.setHtml(_translate("Form", ""))
        self.mytimer.stop()

    def setupUi(self, Form):

        self.frame = QtWidgets.QFrame()
        self.frame.setFixedHeight(119)
        self.frame.setFixedWidth(1920)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("border: 0px")

        self.textBrowser = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 1920, 195))
        self.textBrowser.setObjectName("textBrowser")
       
        Form.gridLayout.addWidget(self.frame,1,0,1,3)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.mytimer = QtCore.QTimer(self.frame)
        self.mytimer.timeout.connect(self.removeMsg)
        self.mytimer.start(10000)
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.textBrowser.setHtml(_translate("Form", "<html><head/>\n"
"<body>\n<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\n"
"<span style=\" font-family:\'Inter\'; font-size:64px; font-weight:696; vertical-align:middle;\">"
"Welcome to Course Management System<br /></span></p></body></html>"))


    


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = CourseInfo()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())
