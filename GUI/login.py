# modified from https://stackoverflow.com/a/22698342

import os
import sys
import pickle
import cv2
from datetime import datetime

from PyQt5.QtCore import Qt, QTimer, QSize, QRect
from PyQt5.QtGui import QIcon, QPixmap, QCursor, QImage
from PyQt5.QtWidgets import QStackedWidget, QWidget, QPushButton, QLabel, QGraphicsDropShadowEffect
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QFrame, QDesktopWidget, QLineEdit
from qtwidgets import AnimatedToggle
from timetable import Timetable
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
        # compute mainwindow variables and write to DB
        def timeToString(time):
            return f'{time.hour}:{time.minute}:{time.second}'

        def dateToString(date):
            return f"{date.year}-{date.month}-{date.day}"
        
        def datetimeToString(datetime):
            # different date format from above
            d = [None, "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            return f"{datetime.year} {d[datetime.month]} {datetime.day}"

        now = datetime.now()
        uiMainWindow.login_time = timeToString(now.time())
        uiMainWindow.login_date = dateToString(now.date())
        uiMainWindow.backend.putLoginInfo(uiMainWindow.stu_id, uiMainWindow.login_time, uiMainWindow.login_date)
        uiMainWindow.email, uiMainWindow.username, uiMainWindow.last_login_time = uiMainWindow.backend.getStudentInfo(uiMainWindow.stu_id)
        uiMainWindow.last_login_time = datetimeToString(uiMainWindow.last_login_time)

        uiMenuBar = MenuBar()
        uiMenuBar.setupUi(uiMainWindow)
        uiWelMsg = WelMsg()
        uiWelMsg.setupUi(uiMainWindow)
    #check if any course within 1 hr
        temp = uiMainWindow.backend.HaveClassIn1Hr(uiMainWindow.stu_id)
        if (temp[0] != 0):
            course_id=temp[0]
            uiCourseInfo = CourseInfo()
            uiCourseInfo.setupUi(uiMainWindow, course_id)
        else: 
            uiTimetable = Timetable()
            uiTimetable.setupUi(uiMainWindow)

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
        self.face_recognition_widget = FaceRecognitionWidget(self.frame, uiMainWindow, self.toDashBoard)

        self.central_widget.addWidget(self.login_widget)
        self.central_widget.addWidget(self.face_recognition_widget)

        uiMainWindow.HLayoutWidget.setGeometry(QRect(0, 0, 1920,1080))
        uiMainWindow.HLayout.addWidget(self.frame)

        self.login_widget.login_button.clicked.connect(lambda:self.login(uiMainWindow))
        self.login_widget.face_recognition_button.clicked.connect(self.to_face_recognition)
        self.face_recognition_widget.return_to_login.clicked.connect(self.to_login)

    def login(self, uiMainWindow):
        UID = self.login_widget.uid_input.text()
        password = self.login_widget.password_input.text()
        query_result = uiMainWindow.backend.checkLoginCredentials(UID, password)
        if query_result != "0000000000":
            uiMainWindow.stu_id = query_result
            self.toDashBoard(uiMainWindow)
        else:
            self.error_message = QLabel("Login Failed!")
            self.error_message.setStyleSheet("QLabel {font-size: 24px; color: red; background-color:#fff}")
            self.error_message.setGeometry(0, 0, 400, 100)
            self.error_message.show()

    def to_face_recognition(self):
        self.central_widget.setCurrentWidget(self.face_recognition_widget)

    def to_login(self):
        if self.face_recognition_widget.device is not None:
            self.face_recognition_widget.device.release()
            self.face_recognition_widget.device = None
            self.face_recognition_widget.cam_feed.clear()
            self.face_recognition_widget.timer.stop()
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
        self.uid_input.setPlaceholderText(' Username')

        self.password_input = QLineEdit()
        self.password_input.setMinimumSize(250, 50)
        self.password_input.setStyleSheet(input_style)
        self.password_input.setPlaceholderText(' Password')
        self.password_input.setEchoMode(QLineEdit.Password)

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

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setOffset(0, 3)
        self.login_button.setGraphicsEffect(shadow)
        shadow2 = QGraphicsDropShadowEffect()
        shadow2.setBlurRadius(10)
        shadow2.setOffset(0, 3)
        self.face_recognition_button.setGraphicsEffect(shadow2)

        padding = QLabel()
        padding.setMaximumHeight(20)
        padding.setStyleSheet("background-color: transparent;")

        login_card_layout = QGridLayout()
        login_card_layout.addWidget(padding, 0, 0, 1, 4)
        login_card_layout.addWidget(self.uid_input, 1, 1, 1, 2)
        login_card_layout.addWidget(self.password_input, 2, 1, 1, 2)
        login_card_layout.addLayout(button_slot, 3, 1, 1, 2)
        login_card_layout.setVerticalSpacing(60)

        self.login_card.setLayout(login_card_layout)

        padding = QLabel()
        padding.setMaximumHeight(200)
        padding.setStyleSheet("background-color: transparent;")
        
        layout.addWidget(self.title, 0, 0, 1, 4)
        layout.addWidget(self.login_card, 1, 1, 1, 2)
        layout.addWidget(padding, 2, 0, 1, 4)

        self.setLayout(layout)

class FaceRecognitionWidget(QWidget):
    def __init__(self, parent, uiMainWindow, toDashBoard):
        super().__init__(parent)

        self.face_cascade = None
        self.recognizer = None

        self.confidence_threshold = 60

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
        self.toggle_button.toggled.connect(lambda: self.connect(uiMainWindow, toDashBoard))

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

        self.flg_conn = False
        self.device = None

    # ~~~~~~~~ connect device ~~~~~~~~
    def connect(self, uiMainWindow, toDashBoard):
        if not os.path.isfile('../FaceRecognition/train.yml'):
            self.error_message = QLabel("Model not found!")
            self.error_message.setStyleSheet("QLabel {font-size: 24px; color: red; background-color:#fff}")
            self.error_message.setGeometry(0, 0, 400, 100)
            self.error_message.show()
            return

        if self.face_cascade is None:
            self.face_cascade = cv2.CascadeClassifier('../FaceRecognition/haarcascade/haarcascade_frontalface_default.xml')
        if self.recognizer is None:
            self.recognizer = cv2.face.LBPHFaceRecognizer_create()
            self.recognizer.read("../FaceRecognition/train.yml")

        self.flg_conn = not self.flg_conn
        if self.flg_conn:
            self.camera_status.setText('Camera On')
            if self.device is None:
                self.device = cv2.VideoCapture(0)
            self.timer = QTimer()
            self.timer.timeout.connect(lambda: self.update(uiMainWindow, toDashBoard))
            self.timer.start(50)
        else:
            self.camera_status.setText('Camera not turned on')
            if self.device is not None:
                self.device.release()
                self.device = None
            self.cam_feed.clear()
            self.timer.stop()
        
        return

    # ~~~~~~~~ update ~~~~~~~~
    def update(self, uiMainWindow, toDashBoard):
        labels = {"person_name": 1}
        with open("../FaceRecognition/labels.pickle", "rb") as f:
            labels = pickle.load(f)
            labels = {v: k for k, v in labels.items()}

        _, frame = self.device.read()
        Qframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        Qframe = QImage(Qframe, Qframe.shape[1], Qframe.shape[0], Qframe.strides[0], QImage.Format_RGB888)
        self.cam_feed.setPixmap(QPixmap.fromImage(Qframe))

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

        for (x, y, w, h) in faces:
            print(x, w, y, h)
            roi_gray = gray[y:y + h, x:x + w]
            # predict the id and confidence for faces
            id_, conf = self.recognizer.predict(roi_gray)

            # If the face is recognized
            if conf >= self.confidence_threshold: # 60
                self.timer.stop()
                uid = labels[id_]
                uiMainWindow.stu_id = uid
                toDashBoard(uiMainWindow)

        return
    
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     app.setStyle('Fusion')
#     window = MainWindow()
#     window.show()
#     window.setFixedSize(1920, 1014)
#     window.moveWindowToCenter()
#     sys.exit(app.exec_())