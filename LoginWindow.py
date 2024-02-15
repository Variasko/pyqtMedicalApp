import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from sqlalchemy.orm import Session
from dbConnectHelper import validatePerson


class Ui_loginWindow(object):

    loggined = False

    def setupUi(self, loginWindow):
        loginWindow.setObjectName("loginWindow")
        loginWindow.resize(520, 273)
        self.centralwidget = QtWidgets.QWidget(loginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loginEnter = QtWidgets.QTextEdit(self.centralwidget)
        self.loginEnter.setGeometry(QtCore.QRect(240, 50, 181, 31))
        self.loginEnter.setStyleSheet("font: 13pt \"Times New Roman\";")
        self.loginEnter.setObjectName("loginEnter")
        self.passwordEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.passwordEdit.setGeometry(QtCore.QRect(240, 120, 181, 31))
        self.passwordEdit.setStyleSheet("font: 13pt \"Times New Roman\";")
        self.passwordEdit.setObjectName("passwordEdit")
        self.loginLabel = QtWidgets.QLabel(self.centralwidget)
        self.loginLabel.setGeometry(QtCore.QRect(100, 60, 47, 13))
        self.loginLabel.setObjectName("loginLabel")
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setGeometry(QtCore.QRect(100, 130, 47, 13))
        self.passwordLabel.setObjectName("passwordLabel")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(200, 190, 111, 31))
        self.loginButton.setObjectName("loginButton")
        loginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslateUi(self, loginWindow):
        _translate = QtCore.QCoreApplication.translate
        loginWindow.setWindowTitle(_translate("loginWindow", "MainWindow"))
        self.loginLabel.setText(_translate("loginWindow", "Логин:"))
        self.passwordLabel.setText(_translate("loginWindow", "Пароль:"))
        self.loginButton.setText(_translate("loginWindow", "Войти"))

    def auth(self):
        #loggined = validatePerson(login, password)
        loggined = validatePerson(login=self.loginEnter.toPlainText(), password=self.passwordEdit.toPlainText())
        print(loggined)
        return loggined

