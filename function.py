import MICPlus
from MICPlus import Ui_functionWindow
from tkinter.messagebox import *

def getField(window: Ui_functionWindow):
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
        return errorField("фамилия")

    if (name == None):
        return errorField("имя")

    if (serial == None):
        return errorField("серия паспорта")

    if (number == None):
        return errorField("номер паспорта")

    if (address == None):
        return errorField("адрес")

    if (insuranceCompany == None):
        return errorField("страховая компания")

    if(medCardNum == None):
        return errorField("номер медицинской карты")

    if(dateGetted == None):
        return errorField("дата получения медицинской карты")

    if(numberInsurance == None):
        return errorField("номер страхового полиса")

    if(dateInsuranceDead == None):
        return errorField("дата окончания полиса")

    if(bitrh == None):
        return errorField("дата рождения")

    if(phoneNum == None):
        return errorField("номер телефона")

    infoAll()

def infoAll():
    showinfo("Все нужные поля заполнены")

def errorField(type):
    showerror("Не все поля заполнены", f"Вы не заполнили поле: '{type}'")



