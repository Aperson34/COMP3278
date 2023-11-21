# -*- coding: utf-8 -*-

# From copying course_info.py
#
# Created by: Alix Hui 
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again. But that's impossible because nobody will use that software to
# edit this file anyway. Do not edit this file unless you know what you are doing.
# Actually edit this file if you like to.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QWidget, QPushButton, QLabel, QApplication
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QFrame, QDesktopWidget, QLineEdit
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QScrollArea

class Profile(object):
    def setupUi(self, MainWindow):

        profile_data = (MainWindow.username, MainWindow.email, MainWindow.last_login_time)
        # [("Chan Tai Man"), ("u3030303@connect.hku.hk"), ("4 Nov 2023 4:52pm")]
        # these should all be datetime.date or datetime.time's
        login_history = MainWindow.backend.getLoginBehaviour(MainWindow.stu_id)
        # [("8 Nov 2023", "1:00pm", "8 Nov 2023", "2:00pm"),
        #                  ("8 Nov 2023", "5:00pm", "8 Nov 2023", "6:00pm"),
        #                  ("9 Nov 2023", "11:00am", "9 Nov 2023", "12:00pm"),
        #                  ("11 Nov 2023", "1:00pm", "11 Nov 2023", "2:00pm"),
        #                  ("12 Nov 2023", "11:00pm", "13 Nov 2023", "12:00am"),
        #                  ("15 Nov 2023", "1:00pm", "15 Nov 2023", "2:00pm"),
        #                  ("15 Nov 2023", "1:00pm", "15 Nov 2023", "2:00pm"),
        #                  ("15 Nov 2023", "3:00pm", "15 Nov 2023", "4:00pm"),
        #                  ("15 Nov 2023", "6:00pm", "15 Nov 2023", "7:00pm"),
        #                  ("15 Nov 2023", "10:00pm", "15 Nov 2023", "11:00pm"),
        #                  ]
        
        self.frame = QtWidgets.QFrame()
        self.frame.setFixedHeight(833)
        self.frame.setFixedWidth(1664)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("border: 3px")
        self.gridLayoutWidget = QtWidgets.QWidget(self.frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1664, 833))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        self.profile_card = ProfileCard(profile_data, MainWindow.stu_id)
        self.login_hist_card = LoginHistoryCard(login_history)

        self.title1 = QLabel("Profile")
        self.title1.setStyleSheet('font-size: 48px;')
        self.title2 = QLabel("Login History")
        self.title2.setStyleSheet('font-size: 48px;')

        padding = QLabel()
        padding.setMinimumHeight(20)
        padding.setStyleSheet("background-color: transparent;")


        self.gridLayout.addWidget(self.title1, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.profile_card, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.title2, 4, 1, 1, 1)
        self.gridLayout.addWidget(self.login_hist_card, 5, 1, 1, 1)
        self.gridLayout.addWidget(padding, 6, 1, 1, 1)
        MainWindow.gridLayout.addWidget(self.frame,2,1,1,1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

class ProfileCard(QFrame):
    def __init__(self, profile_data, UID, parent=None):
        super().__init__(parent)
        layout = QGridLayout()

        self.setStyleSheet('QFrame {background-color: #fff; border: 1px solid grey; border-radius:15px; font-family: inter;} QLabel {border: none; font-weight:bold; font-size: 30px; }')
        self.setFixedWidth(1620)
        self.setFixedHeight(300)
        
        self.UID = QLabel(UID)
        self.name = QLabel(profile_data[0])
        self.email = QLabel(profile_data[1])
        self.last_login_date = QLabel(str(profile_data[2]))

        layout.addWidget(QLabel("UID"), 0, 0, 1, 3)
        layout.addWidget(QLabel("Name"), 1, 0, 1, 3)
        layout.addWidget(QLabel("Email"), 2, 0, 1, 3)
        layout.addWidget(QLabel("Birthday"), 3, 0, 1, 3)

        layout.addWidget(self.UID, 0, 3, 1, 5)
        layout.addWidget(self.name, 1, 3, 1, 5)
        layout.addWidget(self.email, 2, 3, 1, 5)
        layout.addWidget(self.last_login_date, 3, 3, 1, 5)

        self.setLayout(layout)

class LoginHistoryCard(QScrollArea):
    def __init__(self, login_history, parent=None):
        super().__init__(parent)
        layout = QGridLayout()
        
        self.setStyleSheet('QFrame {background-color: #fff; border: 1px solid grey; border-radius:15px; font-family: inter;} QLabel {border: none; font-weight:bold; font-size: 30px; }')
        self.setFixedWidth(1620)
        self.setFixedHeight(300)

        self.horizontalScrollBar().setStyleSheet("QScrollBar {height:0px;}")
        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1659, 469))
        # self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, len(login_history)*130))

        layout = QGridLayout()
        layout.addWidget(QLabel("Login Date                "), 0, 0, 1, 3)
        layout.addWidget(QLabel("Login Time                "), 0, 3, 1, 3)
        layout.addWidget(QLabel("Logout Date               "), 0, 6, 1, 3)
        layout.addWidget(QLabel("Logout Time               "), 0, 9, 1, 3)
        # layout.addWidget(QLabel("Login Duration            "), 0, 12, 1, 3)
        
        # TODO change dummy data into correct format and compute total duration of login
        for i in range(len(login_history)):
            layout.addWidget(QLabel(str(login_history[i][2])), i+1, 0, 1, 3)
            layout.addWidget(QLabel(str(login_history[i][1])), i+1, 3, 1, 3)
            layout.addWidget(QLabel(str(login_history[i][4])), i+1, 6, 1, 3)
            layout.addWidget(QLabel(str(login_history[i][3])), i+1, 9, 1, 3)

        temp = QWidget()
        temp.setLayout(layout)

        self.setWidget(temp)
        # layout.addWidget(self.scrollArea, 0, 0, 1, 1)

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Profile()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())
