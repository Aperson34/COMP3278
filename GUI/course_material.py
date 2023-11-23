# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\course_material.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import datetime

from timetable import Timetable
import webbrowser

class Material_Item:
        
    def __init__(self, scrollAreaWidgetContents, name, i,checkedList, link):
        def openLink(link):
            link = link[2:]
            link =  'https://icms.com'+link
            webbrowser.open(link, new=2)
        def checked(checkedList, i):
            checkedList[i] = not checkedList[i]
        _translate = QtCore.QCoreApplication.translate
        self = QtWidgets.QWidget(scrollAreaWidgetContents)
        self.setGeometry(QtCore.QRect(0, i*130, 1661, 101))
        self.setObjectName("widget")
        checkBox = QtWidgets.QCheckBox(self)
        checkBox.setGeometry(QtCore.QRect(40, 30, 50, 50))
        checkBox.setText("")
        checkBox.setIconSize(QtCore.QSize(50, 48))
        checkBox.setObjectName("checkBox_1")
        checkBox.clicked.connect(lambda:checked(checkedList, i))
        materialButton = QtWidgets.QPushButton(self)
        materialButton.setGeometry(QtCore.QRect(100, 20, 1501, 61))
        materialButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        materialButton.clicked.connect(lambda:openLink(link))
        materialButton.setStyleSheet("border: none; text-align:left; background-color:#F4F4F4")
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        materialButton.setFont(font)
        materialButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        materialButton.setObjectName("label_1")
        materialButton.setText(_translate("Form", name))
        checkedList.append(False)

class Material_List(object):
    def setupUi(self, MainWindow ,course_id):
        #fetch course material data with given course_id
        self.sqlMaterialData = MainWindow.backend.getCourseMaterial(MainWindow.stu_id,course_id)
        # [("COMP3278","Lecture 1 note", datetime.date(2023,11,16), datetime.time(15,30,00,00)),
        #            ("COMP3278","Tutoraial 1 note", datetime.date(2023,11,16), datetime.time(15,30,00,00)),
        #            ("COMP3278","Lecture 2 note", datetime.date(2023,11,16), datetime.time(15,30,00,00)),
        #            ("COMP3278","Tutoraial 2 note", datetime.date(2023,11,16), datetime.time(15,30,00,00)),
        #            ("COMP3278","Lecture 3 note", datetime.date(2023,11,16), datetime.time(15,30,00,00)),
        #            ("COMP3278","Tutoraial 3 note", datetime.date(2023,11,16), datetime.time(15,30,00,00))
        #            ,("COMP3278","Lecture 4 note", datetime.date(2023,11,16), datetime.time(15,30,00,00))
        #            ,("COMP3278","Tutoraial 4 note", datetime.date(2023,11,16), datetime.time(15,30,00,00))]
        self.frame = QtWidgets.QFrame(MainWindow)
        self.frame.setFixedHeight(833)
        self.frame.setFixedWidth(1664)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("border: 0px")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(1269, 684, 395, 73))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda:self.sendEmail(MainWindow,course_id))
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
        self.scrollArea.horizontalScrollBar().setStyleSheet("QScrollBar {height:0px;}")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1659, 469))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, len(self.sqlMaterialData)*130))
        
        self.materialItem = []
        self.checkedList = []
        for i in range(0,len(self.sqlMaterialData)):
            self.materialItem.append(Material_Item(self.scrollAreaWidgetContents,self.sqlMaterialData[i][0], i, self.checkedList ,self.sqlMaterialData[i][1]))

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.gridLayout.addWidget(self.frame,2,1,1,1)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Send to Email"))
        self.Title.setText(_translate("Form", "COMP3278 Material"))

    def sendEmail(self,MainWindow,course_id):
        materialNeeded = []
        for i in range(0,len(self.sqlMaterialData )):
            if self.checkedList[i]:
                materialNeeded.append(self.sqlMaterialData[i][0])
        MainWindow.backend.sendemail(materialNeeded, MainWindow.stu_id,course_id)
        self.toCourseList(MainWindow)
    def toCourseList(self,MainWindow):
        item = MainWindow.gridLayout.takeAt(2)
        if item is not None:
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        uiCourseMaterial = Timetable()
        uiCourseMaterial.setupUi(MainWindow)
