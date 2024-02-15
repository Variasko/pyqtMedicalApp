from LoginWindow import Ui_loginWindow
from menuWindow import *
from dbConnectHelper import validatePerson
from PyQt5 import QtCore, QtGui, QtWidgets
import sys



def login():
    global functionWindow
    functionWindow = QtWidgets.QMainWindow()
    ui = Ui_functionWindow()
    ui.setupUi(functionWindow)



    try:
        a = Ui_loginWindow()
        auth = a.auth()
    except Exception as e:
        print(e)

    functionWindow.show()
    LoginWindow.hide()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_loginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    ui.loginButton.clicked.connect(login)
    sys.exit(app.exec_())
