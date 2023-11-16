# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\course_material.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import datetime

sqlMaterialData = [("COMP3278","Lecture 1 note", datetime.date(2023,11,16), datetime.time(15,30,00,00)),
                   ("COMP3278","Tutoraial 1 note", datetime.date(2023,11,16), datetime.time(15,30,00,00)),
                   ("COMP3278","Lecture 2 note", datetime.date(2023,11,16), datetime.time(15,30,00,00)),
                   ("COMP3278","Tutoraial 2 note", datetime.date(2023,11,16), datetime.time(15,30,00,00)),
                   ("COMP3278","Lecture 3 note", datetime.date(2023,11,16), datetime.time(15,30,00,00)),
                   ("COMP3278","Tutoraial 3 note", datetime.date(2023,11,16), datetime.time(15,30,00,00))
                   ,("COMP3278","Lecture 4 note", datetime.date(2023,11,16), datetime.time(15,30,00,00))
                   ,("COMP3278","Tutoraial 4 note", datetime.date(2023,11,16), datetime.time(15,30,00,00))]

class Material_Item:
    def __init__(self, scrollAreaWidgetContents, name, i):
        _translate = QtCore.QCoreApplication.translate
        self = QtWidgets.QWidget(scrollAreaWidgetContents)
        self.setGeometry(QtCore.QRect(0, i*130, 1661, 101))
        self.setObjectName("widget")
        checkBox = QtWidgets.QCheckBox(self)
        checkBox.setGeometry(QtCore.QRect(40, 30, 50, 50))
        checkBox.setText("")
        checkBox.setIconSize(QtCore.QSize(50, 48))
        checkBox.setObjectName("checkBox_1")
        label = QtWidgets.QLabel(self)
        label.setGeometry(QtCore.QRect(100, 20, 1501, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        label.setFont(font)
        label.setObjectName("label_1")
        label.setText(_translate("Form", name))

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 1080)
        Form.setMinimumSize(QtCore.QSize(1920, 1080))
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(100, 320, 1664, 757))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(1269, 684, 395, 73))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.Title = QtWidgets.QLabel(self.frame)
        self.Title.setGeometry(QtCore.QRect(0, 0, 1664, 110))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setGeometry(QtCore.QRect(0, 110, 1661, 521))
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1659, 469))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, len(sqlMaterialData)*130))
        
        self.materialItem = []
        for i in range(0,len(sqlMaterialData)):
            self.materialItem.append(Material_Item(self.scrollAreaWidgetContents, sqlMaterialData[i], i))

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Send to Email"))
        self.Title.setText(_translate("Form", "COMP3278 Material"))
      


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
