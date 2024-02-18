import sys
from PyQt5 import QtCore, QtGui, QtWidgets
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

        self.registerButton = QtWidgets.QPushButton(self.centralwidget)  # Добавляем кнопку "Зарегистрироваться"
        self.registerButton.setGeometry(QtCore.QRect(320, 190, 111, 31))
        self.registerButton.setObjectName("registerButton")
        self.registerButton.setText("Зарегистрироваться")

        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel.setGeometry(QtCore.QRect(100, 160, 300, 20))
        self.errorLabel.setObjectName("errorLabel")
        self.errorLabel.setStyleSheet("color: red")

        loginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslateUi(self, loginWindow):
        loginWindow.setWindowTitle("Авторизация")  # Убираем использование _translate
        self.loginLabel.setText("Логин:")  # Убираем использование _translate
        self.passwordLabel.setText("Пароль:")  # Убираем использование _translate
        self.loginButton.setText("Войти")  # Убираем использование _translate

    def auth(self):
        try:
            login = self.loginEnter.toPlainText()
            password = self.passwordEdit.toPlainText()

            if not login or not password:
                self.errorLabel.setText("Логин и пароль должны быть заполнены")
            elif not validatePerson(login, password):
                self.errorLabel.setText("Пользователь не зарегистрирован")
            else:
                self.errorLabel.setText("Успешный вход")  # Здесь можно добавить логику для успешной авторизации
        except Exception as e:
            self.errorLabel.setText(str(e) + " authentication")
# Sample function to simulate the validatePerson function
def validatePerson(login, password):
    return True  # Placeholder return, actual validation logic should be implemented
