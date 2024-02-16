from LoginWindow import Ui_loginWindow
from MICPlus import Ui_functionWindow
from dbConnectHelper import validatePerson
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from function import *


def login(L):
    global functionWindow
    functionWindow = QtWidgets.QMainWindow()
    ui = Ui_functionWindow(functionWindow)

    auth = False

    auth = uiL.auth(uiL.loginEnter.toPlainText(), uiL.passwordEdit.toPlainText())
    print(auth)

    try:
        if auth:
            print("Вы авторизованы")
            functionWindow.show()
            L.hide()

            ui.confirmAddPatientButton.clicked.connect(lambda: getData(ui))


    except Exception as e:
        print(e)

def getData(window):
    getField(window)


if __name__ == "__main__":
    global uiL
    try:
        app = QtWidgets.QApplication(sys.argv)
        LoginWindow = QtWidgets.QMainWindow()
        uiL = Ui_loginWindow(LoginWindow)
        LoginWindow.show()
        uiL.loginButton.clicked.connect(lambda: login(LoginWindow))
        sys.exit(app.exec_())
    except Exception as e:
        print(e)
