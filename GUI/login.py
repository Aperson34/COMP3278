# modified from https://stackoverflow.com/a/22698342

import os
import sys 

from PyQt5.QtCore import Qt, QTimer, QSize, QRect,QMetaObject
from PyQt5.QtGui import QIcon, QPixmap, QCursor
from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QWidget, QPushButton, QLabel, QApplication
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QFrame, QDesktopWidget, QLineEdit
from qtwidgets import AnimatedToggle
from course_info import CourseInfo

from menuBar import MenuBar
from welcomeMsg import WelMsg

class MainWindow(object):
    #after login successfully, please run this function
    def toDashBoard(self,uiMainWindow):
        self.central_widget.deleteLater()
        self.frame.deleteLater()
        uiMainWindow.HLayoutWidget.setGeometry(QRect(0, 0, 0, 0))
        #After login
        uiMenuBar = MenuBar()
        uiMenuBar.setupUi(uiMainWindow)
        uiWelMsg = WelMsg()
        uiWelMsg.setupUi(uiMainWindow)
    #check if any course within 1 hr
    #if yes, return course_id
        course_id=''
        if (True):
            uiCourseInfo = CourseInfo()
            uiCourseInfo.setupUi(uiMainWindow, course_id)
    # else:
    #     timtable()

    def setupUi(self,uiMainWindow):
        self.frame = QFrame()
        self.frame.setFixedHeight(1080)
        self.frame.setFixedWidth(1920)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        
        # use the stacked widget as a means to switch between screens
        self.central_widget = QStackedWidget(self.frame)
        uiMainWindow.setCentralWidget(self.central_widget)
        
        self.frame.setStyleSheet('background-color: #ffffff;')
        self.frame.setWindowTitle('Course Management System')

        self.login_widget = LoginWidget(self.frame)
        self.face_recognition_widget = FaceRecognitionWidget(self.frame)
        self.logged_in_widget = LoggedWidget(self.frame)

        self.central_widget.addWidget(self.login_widget)
        self.central_widget.addWidget(self.face_recognition_widget)
        self.central_widget.addWidget(self.logged_in_widget)


        uiMainWindow.HLayoutWidget.setGeometry(QRect(0, 0, 1920,1080))
        uiMainWindow.HLayout.addWidget(self.frame)

        self.login_widget.login_button.clicked.connect(lambda:self.login(uiMainWindow))
        self.login_widget.face_recognition_button.clicked.connect(self.to_face_recognition)
        self.face_recognition_widget.return_to_login.clicked.connect(self.to_login)

    def login(self, uiMainWindow):
        # self.flg_login = not self.flg_login
        # if self.flg_login:
        #     username = self.login_page.uid_input.text()
        #     password = self.login_page.password_input.text()
        #     if not username:
        #         self.username.setText('root')
        #     if password == '':
        #         self.password.setText('1203')

        #     if self.conn is None:
        #         self.conn = mysql.connector.connect(host="localhost", port=3306, 
        #             user=self.username.text(), passwd=self.password.text())
        #     self.btn_login.setStyleSheet(self.btn_login_style_1)
        #     self.btn_login.setText('Log out')
        # else:
        #     if self.conn is not None:
        #         self.conn = None
        #     self.btn_login.setStyleSheet(self.btn_login_style_0)
        #     self.btn_login.setText('Log in')

        # uiMainWindow.stu_id = checkLoginCredentials(idk the pram)
        self.central_widget.setCurrentWidget(self.logged_in_widget)

    def to_face_recognition(self):
        self.central_widget.setCurrentWidget(self.face_recognition_widget)

    def to_login(self):
        self.central_widget.setCurrentWidget(self.login_widget)

    def moveWindowToCenter(self):
        window_rect = self.frameGeometry()
        screen_cent = QDesktopWidget().availableGeometry().center()
        window_rect.moveCenter(screen_cent)
        self.move(window_rect.topLeft())

class LoginWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        layout = QGridLayout()

        self.title = QLabel("Course Management System")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet('QLabel {font-family: inter; font-size: 96px; color: #5B3256; font-weight: bold;}')

        # create login card
        self.login_card = QWidget()
        self.login_card.setStyleSheet('QWidget {background-color: qlineargradient(spread: pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #E3DCE2 stop:1 #ffffff); border: none; border-radius: 30px}')

        input_style = 'QLineEdit {background-color: white; border: 1px solid black; border-radius: 12px; font-family: inter; font-size: 24px;}'

        self.uid_input = QLineEdit()
        self.uid_input.setMinimumSize(250, 50)
        self.uid_input.setStyleSheet(input_style)
        self.uid_input.setPlaceholderText(' UID')

        self.password_input = QLineEdit()
        self.password_input.setMinimumSize(250, 50)
        self.password_input.setStyleSheet(input_style)
        self.password_input.setPlaceholderText(' Password')

        # create the button spacing box
        button_slot = QHBoxLayout()

        self.button_style_0 = 'QPushButton {background-color: #5B3256; border: none; border-radius: 8px; color: #ffffff; font-family: inter; font-size: 24px; font-weight:bold; }'
        self.button_style_1 = 'QPushButton {background-color: #ff6464; border: none; border-radius: 8px; color: #ffffff; font-family: inter; font-size: 24px; font-weight:bold; }'
        
        self.login_button = QPushButton('Login')
        self.login_button.setMinimumHeight(50)
        self.login_button.setStyleSheet(self.button_style_0)
        self.login_button.setCursor(QCursor(Qt.PointingHandCursor))
        
        self.face_recognition_button = QPushButton()
        self.face_recognition_button.setMinimumHeight(50)
        self.face_recognition_button.setStyleSheet(self.button_style_0)
        self.face_recognition_button.setIcon(QIcon('facercnt.png'))
        self.face_recognition_button.setIconSize(QSize(50, 50))
        self.face_recognition_button.setToolTip('Use face to login')
        self.face_recognition_button.setCursor(QCursor(Qt.PointingHandCursor))

        button_slot.addWidget(self.login_button, stretch=2)
        button_slot.addStretch(1)
        button_slot.addWidget(self.face_recognition_button, stretch=2)


        padding = QLabel()
        padding.setMaximumHeight(20)
        padding.setStyleSheet("background-color: transparent;")

        login_card_layout = QGridLayout()
        login_card_layout.addWidget(padding, 0, 0, 1, 4)
        login_card_layout.addWidget(self.uid_input, 1, 1, 1, 2)
        login_card_layout.addWidget(self.password_input, 2, 1, 1, 2)
        # login_card_layout.addWidget(self.login_button, 3, 1, 1, 1)
        # login_card_layout.addWidget(self.face_recognition_button, 3, 2, 1, 1)
        login_card_layout.addLayout(button_slot, 3, 1, 1, 2)
        login_card_layout.setVerticalSpacing(60)

        self.login_card.setLayout(login_card_layout)

        self.button2 = QPushButton('try to change text')
        self.display1 = QLabel("unchanged text")
        self.button2.clicked.connect(self.change_text)

        padding = QLabel()
        padding.setMaximumHeight(200)
        padding.setStyleSheet("background-color: transparent;")
        
        layout.addWidget(self.title, 0, 0, 1, 4)
        layout.addWidget(self.login_card, 1, 1, 1, 2)
        layout.addWidget(padding, 2, 0, 1, 4)

        self.setLayout(layout)

    def change_text(self):
        self.display1.setText("modified text")

class FaceRecognitionWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        layout = QGridLayout()
        self.setStyleSheet('font-family: inter; font-weight:bold; font-size: 48px;')

        self.cam_feed = QLabel()
        self.cam_feed.setMinimumSize(640, 480)
        self.cam_feed.setAlignment(Qt.AlignCenter)
        self.cam_feed.setFrameStyle(QFrame.StyledPanel)
        self.cam_feed.setStyleSheet('QLabel {background-color: #000000;}')
        
        self.button_style_0 = 'QPushButton {background-color: #5B3256; border: none; border-radius: 8px; font-size: 24px; color: #ffffff;}'

        self.title = QLabel("Course Management System")
        self.title.setStyleSheet('QLabel {font-size: 64px; color: #5B3256;}')

        self.message = QLabel("Login using face recognition.\n\nThis operation requires you to have\na camera on your device.\nIf your device does not have a\ncamera, please use another device\nto login to the system.")
        
        self.camera_status = QLabel("Camera not turned on")
        self.camera_status.setStyleSheet('font-size: 36px;')
        
        self.toggle_label = QLabel("Use camera")
        self.toggle_label.setStyleSheet('font-size: 36px;')

        self.toggle_button = AnimatedToggle(
            checked_color="#3399ff",
            pulse_checked_color="#443399ff"
        )

        self.return_to_login = QPushButton('Return to Login')
        self.return_to_login.setMinimumHeight(80)
        self.return_to_login.setMaximumWidth(400)
        self.return_to_login.setStyleSheet(self.button_style_0)
        self.return_to_login.setCursor(QCursor(Qt.PointingHandCursor))

        padding = QLabel()
        padding.setMaximumHeight(80)
        padding.setStyleSheet("background-color: transparent;")

        padding2 = QLabel()
        padding2.setMaximumHeight(80)
        padding2.setStyleSheet("background-color: transparent;")

        message_area = QVBoxLayout()
        cam_area = QGridLayout()

        message_area.addStretch(1)
        message_area.addWidget(self.title, stretch=1)
        message_area.addWidget(self.message, stretch=5)
        message_area.addWidget(self.return_to_login, stretch=1)
        message_area.addStretch(1)

        cam_area.addWidget(self.cam_feed, 0, 0, 6, 2)
        cam_area.addWidget(self.camera_status, 6, 0, 1, 2)
        cam_area.addWidget(self.toggle_label, 7, 0, 1, 1)
        cam_area.addWidget(self.toggle_button, 7, 1, 1, 1)

        layout.addWidget(padding, 0, 0, 1, 12)
        layout.addLayout(message_area, 1, 1, 4, 6)
        layout.addLayout(cam_area, 1, 6, 4, 4)
        layout.addWidget(padding2, 5, 0, 1, 12)

        self.setLayout(layout)

    # def connect(self,uiMainWindow):

    #### plz put stu_id in here: uiMainWindow.stu_id

    #     if self.flg_recd:
    #         self.record()
    #     self.flg_conn = not self.flg_conn
    #     if self.flg_conn:
    #         self.btn_conn.setStyleSheet(self.btn_conn_style_1)
    #         self.btn_conn.setText('Disconnect Device')
    #         if self.device is None:
    #             self.device = cv2.VideoCapture(0)
    #         self.timer = QTimer()
    #         self.timer.timeout.connect(self.update)
    #         self.timer.start(50)
    #     else:
    #         self.btn_conn.setStyleSheet(self.btn_conn_style_0)
    #         self.btn_conn.setText('Connect Device')
    #         if self.device is not None:
    #             self.device.release()
    #             self.device = None
    #         self.cam_feed.clear()
    #         self.timer.stop()
        
    #     return
    
class LoggedWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        layout = QHBoxLayout()
        self.label = QLabel('logged in!')
        layout.addWidget(self.label)
        self.setLayout(layout)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     app.setStyle('Fusion')
#     window = MainWindow()
#     window.show()
#     window.setFixedSize(1920, 1014)
#     window.moveWindowToCenter()
#     sys.exit(app.exec_())