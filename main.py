from LoginWindow import Ui_loginWindow
from menuWindow import *
from dbConnectHelper import validatePerson
from PyQt5 import QtCore, QtGui, QtWidgets
import sys



def asd():
    global functionWindow
    functionWindow = QtWidgets.QMainWindow()
    ui = Ui_functionWindow()
    ui.setupUi(functionWindow)

    a = Ui_loginWindow.auth()


    functionWindow.show()
    LoginWindow.hide()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_loginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()

    ui.loginButton.clicked.connect(asd)




    sys.exit(app.exec_())
