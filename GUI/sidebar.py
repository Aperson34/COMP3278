# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\sidebar.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from profile import Profile
from PyQt5 import QtCore, QtGui, QtWidgets

from course_list import Course_List
from timetable import Timetable
from datetime import datetime

class Sidebar(QtWidgets.QWidget):
    def logout(self, MainWindow):
        #Please follow this format: MainWindow.backend.putLogoutInfo("3035788621", "10:20:03", "2023-11-22", "12:02:03", "2023-11-22")
        MainWindow.backend.putLogoutInfo(MainWindow.stu_id, MainWindow.login_time.time(), MainWindow.login_time.date(), datetime.now().time(), datetime.now().date())
        MainWindow.close()
    def setupUi(self, MainWindow):
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.frame = QtWidgets.QFrame()
        self.frame.setStyleSheet('background-color: rgb(206,194,204)') 
        self.frame.setFixedHeight(1080)
        self.frame.setFixedWidth(709)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(62, 970, 585, 73))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet('background-color: rgb(91, 50, 86)')  
        self.pushButton.setFont(font) 
        self.pushButton.clicked.connect(lambda:self.logout(MainWindow))

        self.backButton = QtWidgets.QPushButton(self.frame)
        self.backButton.setGeometry(QtCore.QRect(600, 0, 100, 100))
        self.backButton.setObjectName("backButton")
        self.backButton.setStyleSheet('background-color: rgb(91, 50, 86)')  
        self.backButton.setFont(font) 
        self.backButton.clicked.connect(lambda:self.hideSideBar(MainWindow))

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(50, 0, 480, 91))
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")

        self.Course_List = QtWidgets.QPushButton(self.frame)
        self.Course_List.setGeometry(QtCore.QRect(50, 200, 601, 91))
        self.Course_List.setFont(font)
        self.Course_List.setObjectName("label_2")
        self.Course_List.setStyleSheet(" background-color: rgb(206,194,204);  border: none; ")  
        self.Course_List.clicked.connect(lambda:self.toCourse_List(MainWindow))

        self.Timetable = QtWidgets.QPushButton(self.frame)
        self.Timetable.setGeometry(QtCore.QRect(50, 350, 601, 91))
        self.Timetable.setFont(font)
        self.Timetable.setStyleSheet(" background-color: rgb(206,194,204);  border: none; ")  
        self.Timetable.setObjectName("Timetable")
        self.Timetable.clicked.connect(lambda:self.toTimetable(MainWindow))

        self.Profile = QtWidgets.QPushButton(self.frame)
        self.Profile.setGeometry(QtCore.QRect(50, 500, 601, 91))
        self.Profile.setFont(font)
        self.Profile.setStyleSheet(" background-color: rgb(206,194,204);  border: none; ")  
        self.Profile.setObjectName("Profile")
        self.Profile.clicked.connect(lambda:self.toProfile(MainWindow))

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("Form", "Logout"))
        self.label.setText(_translate("Form", "Course Management System"))
        self.Course_List.setText(_translate("Form", "Course List"))
        self.Timetable.setText(_translate("Form", "Timetable"))
        self.Profile.setText(_translate("Form", "Profile"))
        self.backButton.setText(_translate("Form", "Back"))
    
    def hideSideBar(self,MainWindow):
        while MainWindow.HLayout.count():
            item = MainWindow.HLayout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                MainWindow.HLayoutWidget.setGeometry(QtCore.QRect(0, 0, 0, 0))
        MainWindow.HLayoutWidget.setGeometry(QtCore.QRect(0, 0, 0, 0))
    
    def toCourse_List(self,MainWindow):
        item = MainWindow.gridLayout.takeAt(2)
        if item is not None:
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        self.hideSideBar(MainWindow)
        uiCourseMaterial = Course_List()
        uiCourseMaterial.setupUi(MainWindow)

    def toTimetable(self,MainWindow):
        item = MainWindow.gridLayout.takeAt(2)
        if item is not None:
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        self.hideSideBar(MainWindow)
        uiTimetable = Timetable()
        uiTimetable.setupUi(MainWindow)
    
    def toProfile(self,MainWindow):
        item = MainWindow.gridLayout.takeAt(2)
        if item is not None:
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        self.hideSideBar(MainWindow)
        uiProfile = Profile()
        uiProfile.setupUi(MainWindow)
