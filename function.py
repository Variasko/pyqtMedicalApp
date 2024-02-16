import MICPlus
from MICPlus import Ui_functionWindow
from tkinter.messagebox import *
from PyQt5.QtWidgets import QDialog
from fieldError import *

def getField(window: MICPlus):
    try:
        #self
        surname = window.surnameAddNewPatienLineEdit_2.text()
        name = window.nameAddNewPatientLineEdit_2.text()
        patronymic = window.patronymicAddNewPatientLineEdit_2.text()

        #pasport
        serial = window.pasportSerialAddNewPatientLineEdit_2.text()
        number = window.pasportNumberAddNewPatientLineEdit_2.text()

        #birth, phoneNum
        bitrh = window.birthdayAddNewPatientDatepicker_2.text()
        phoneNum = window.telephoneNumberAddNewPatientLineEdit_2.text()

        #addres and work
        address = window.addressAddNewPatientLabelTextEdit_2.toPlainText()
        workPlace = window.workPlaceAddNewPatientLineEdit_2.text()

        #email
        email = window.emailAddNewPatientLineEdit_2.text()
        insuranceCompany = window.insuranceCompanyAddNewPatientLineEdit_2.text()

        #medicalCard
        medCardNum = window.numberMedicalCardAddNewPatientLineEdit_2.text()
        dateGetted = window.dateGetMedicalCardAddNewPatientDatepicker_2.text()

        #insurancePolicy
        numberInsurance = window.insuranceCompanyAddNewPatientLineEdit_2.text()
        dateInsuranceDead = window.dateDeadInsurancePolicAddNewPatientDatepicker_2.text()

        #visit
        dateLastVisit = window.dateLastVisitAddNewPatientDatepicker_2.text()
        dateNextVisit = window.dateNextVisitAddNewPatientDatepicker_2.text()

        if (surname == None):
            errorField("фамилия")
            return 0

        if (name == None):
            errorField("имя")
            return 0

        if (serial == None):
            errorField("серия паспорта")
            return 0

        if (number == None):
            errorField("номер паспорта")
            return 0

        if (address == None):
            errorField("адрес")
            return 0

        if (insuranceCompany == None):
            errorField("страховая компания")
            return 0

        if(medCardNum == None):
            errorField("номер медицинской карты")
            return 0

        if(dateGetted == None):
            errorField("дата получения медицинской карты")
            return 0

        if(numberInsurance == None):
            errorField("номер страхового полиса")
            return 0

        if(dateInsuranceDead == None):
            errorField("дата окончания полиса")
            return 0

        if(bitrh == None):
            errorField("дата рождения")
            return 0

        if(phoneNum == None):
            errorField("номер телефона")
            return 0

    except Exception as e:
        print(e, "", "function")

def errorField(type):
    window = QDialog()

    ui = Ui_Dialog(window)

    window.show()



