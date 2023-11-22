# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\timetable.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import math
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime

class ClassItem(QtWidgets.QTableWidgetItem):
    def __init__(self, text):
        super().__init__()
        _translate = QtCore.QCoreApplication.translate
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.setBackground(brush)
        self.setText(_translate("Form",text))

class Timetable(object):
    def setupUi(self, Form):
        self.sqlCourseData =Form.backend.getTimeTableDisplayData(Form.stu_id) 
        
        self.frame = QtWidgets.QFrame()
        self.frame.setFixedHeight(833)
        self.frame.setFixedWidth(1664)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1664, 833))
        self.tableWidget.setDisabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        

        for i in self.sqlCourseData:
            begin = datetime.datetime.combine(datetime.date.today(), datetime.time(9,30,00,00))
            dateTimeA = datetime.datetime.combine(datetime.date.today(), (datetime.datetime.min + i[5]).time())
            dateTimeB = datetime.datetime.combine(datetime.date.today(), (datetime.datetime.min + i[4]).time())
            dateTimeDifference = dateTimeA - dateTimeB 
            dateTimeDifferenceInHours = math.ceil(dateTimeDifference.total_seconds() / 3600)
            startTime = dateTimeB - begin 
            startCell = math.ceil(startTime.total_seconds() / 3600) 
            for j in range(0,dateTimeDifferenceInHours):
                classItem = ClassItem(i[1]+' '+i[2])
                week =(i[3].weekday() + 1)%7
                self.tableWidget.setItem(startCell+j, week, classItem)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)

        self.tableWidget.horizontalHeader().setDefaultSectionSize(220)
        self.tableWidget.verticalHeader().setDefaultSectionSize(80)
        Form.gridLayout.addWidget(self.frame,2,1,1,1)

        self.retranslateUi(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "09:30-10:30"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "10:30-11:30"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "11:30-12:30"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "12:30-13:30"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "13:30-14:30"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "14:30-15:30"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Form", "15:30-16:30"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Form", "16:30-17:30"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Form", "17:30-18:30"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Sun"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Mon"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Tue"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Wed"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Thu"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Fri"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Sat"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
