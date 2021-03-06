# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path

path = str(Path.cwd())


class Ui_SignupWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 610)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("%s/img/logo.png" % path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: #fff; border-radius: 5px;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(125, 0, 250, 250))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("%s/img/typing.png" % path))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.setGeometry(QtCore.QRect(460, 10, 30, 30))
        self.btn_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_close.setStyleSheet("background:none;")
        self.btn_close.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("%s/img/close.png" % path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon1)
        self.btn_close.setIconSize(QtCore.QSize(20, 20))
        self.btn_close.setObjectName("btn_close")
        self.btn_minimze = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minimze.setGeometry(QtCore.QRect(430, 10, 30, 30))
        self.btn_minimze.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_minimze.setStyleSheet("background:none;")
        self.btn_minimze.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("%s/img/minimize.png" % path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_minimze.setIcon(icon2)
        self.btn_minimze.setIconSize(QtCore.QSize(20, 20))
        self.btn_minimze.setObjectName("btn_minimze")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 250, 500, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setStyleSheet("color: #010A1A;")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.usernamelb = QtWidgets.QLabel(self.centralwidget)
        self.usernamelb.setGeometry(QtCore.QRect(80, 300, 100, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.usernamelb.setFont(font)
        self.usernamelb.setStyleSheet("color: #010A1A;")
        self.usernamelb.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.usernamelb.setObjectName("usernamelb")
        self.passlb = QtWidgets.QLabel(self.centralwidget)
        self.passlb.setGeometry(QtCore.QRect(80, 400, 100, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.passlb.setFont(font)
        self.passlb.setStyleSheet("color: #010A1A;")
        self.passlb.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.passlb.setObjectName("passlb")
        self.username_en = QtWidgets.QLineEdit(self.centralwidget)
        self.username_en.setGeometry(QtCore.QRect(190, 300, 220, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.username_en.setFont(font)
        self.username_en.setStyleSheet("background-color: #DEDEDE;color: #010A1A;")
        self.username_en.setObjectName("username_en")
        self.password_en = QtWidgets.QLineEdit(self.centralwidget)
        self.password_en.setGeometry(QtCore.QRect(190, 400, 220, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.password_en.setFont(font)
        self.password_en.setStyleSheet("background-color: #DEDEDE; color: #010A1A;")
        self.password_en.setObjectName("password_en")
        self.btn_signup = QtWidgets.QPushButton(self.centralwidget)
        self.btn_signup.setGeometry(QtCore.QRect(80, 520, 330, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.btn_signup.setFont(font)
        self.btn_signup.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_signup.setStyleSheet("background-color: #0088CC; color: #fff;")
        self.btn_signup.setObjectName("btn_signup")
        self.acountlb = QtWidgets.QLabel(self.centralwidget)
        self.acountlb.setGeometry(QtCore.QRect(160, 570, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.acountlb.setFont(font)
        self.acountlb.setStyleSheet("color: #010A1A;")
        self.acountlb.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.acountlb.setObjectName("acountlb")
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(290, 570, 61, 31))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.btn_login.setFont(font)
        self.btn_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_login.setStyleSheet("QPushButton{\n"
"background: none; color: #0088CC;  text-decoration: none;\n"
"}\n"
"QPushButton:hover{\n"
" text-decoration: underline;\n"
"}")
        self.btn_login.setObjectName("btn_login")
        self.repasslb = QtWidgets.QLabel(self.centralwidget)
        self.repasslb.setGeometry(QtCore.QRect(80, 450, 105, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.repasslb.setFont(font)
        self.repasslb.setStyleSheet("color: #010A1A;")
        self.repasslb.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.repasslb.setObjectName("repasslb")
        self.repassword_en = QtWidgets.QLineEdit(self.centralwidget)
        self.repassword_en.setGeometry(QtCore.QRect(190, 450, 220, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.repassword_en.setFont(font)
        self.repassword_en.setStyleSheet("background-color: #DEDEDE; color: #010A1A;")
        self.repassword_en.setObjectName("repassword_en")
        self.alarmlb = QtWidgets.QLabel(self.centralwidget)
        self.alarmlb.setGeometry(QtCore.QRect(0, 490, 500, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.alarmlb.setFont(font)
        self.alarmlb.setStyleSheet("color: #d1131f;")
        self.alarmlb.setText("")
        self.alarmlb.setAlignment(QtCore.Qt.AlignCenter)
        self.alarmlb.setObjectName("alarmlb")
        self.email_en = QtWidgets.QLineEdit(self.centralwidget)
        self.email_en.setGeometry(QtCore.QRect(190, 350, 220, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.email_en.setFont(font)
        self.email_en.setStyleSheet("background-color: #DEDEDE;color: #010A1A;")
        self.email_en.setObjectName("email_en")
        self.emaillb = QtWidgets.QLabel(self.centralwidget)
        self.emaillb.setGeometry(QtCore.QRect(80, 350, 100, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.emaillb.setFont(font)
        self.emaillb.setStyleSheet("color: #010A1A;")
        self.emaillb.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.emaillb.setObjectName("emaillb")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_close.clicked.connect(MainWindow.close)
        self.btn_minimze.clicked.connect(MainWindow.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Online Typing"))
        self.title.setText(_translate("MainWindow", "SIGN UP"))
        self.usernamelb.setText(_translate("MainWindow", "Username:"))
        self.passlb.setText(_translate("MainWindow", "Password:"))
        self.btn_signup.setText(_translate("MainWindow", "Sign up"))
        self.acountlb.setText(_translate("MainWindow", "Already have an acount?"))
        self.btn_login.setText(_translate("MainWindow", "Log in"))
        self.repasslb.setText(_translate("MainWindow", "Reapet Password:"))
        self.emaillb.setText(_translate("MainWindow", "Email:"))
