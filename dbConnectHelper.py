from sqlalchemy import *
from psycopg2 import *
from sqlalchemy.orm import Session
from Model.User import *
from Model.Patient import *

postgresqlDB = "postgresql://postgres:1@127.0.0.1:5433/MedicalDatabase"

engine = create_engine(postgresqlDB, echo=True)

class Base(DeclarativeBase): pass
Base.metadata.create_all(bind=engine)
def validatePerson(login, password):
    with Session(autoflush=False, bind=engine) as db:
        users = db.query(User).all()

        print(login, password)

        isLoggined = False

        for i in users:
            if (i.login == login and i.password == password):
                print(1)
                return True


def addPatient(surname=None, name=None, patronymic=None, serial=None, number=None, bitrh=None, phoneNum=None,
               address=None, workPlace=None, email=None, insuranceCompany=None, medCardNum=None, dateGetted=None,
               numberInsurance=None, dateInsuranceDead=None, dateLastVisit=None, dateNextVisit=None):
    with Session(autoflush=False, bind=engine) as db:
        tom = Patient(surname=surname, name=name, patronymic=patronymic, serial=serial, number=number, bitrh=bitrh, phoneNum=phoneNum, address=address, workPlace=workPlace, email=email,
                      insuranceCompany=insuranceCompany, medCardNum=medCardNum, dateGetted=dateGetted, numberInsurance=numberInsurance, dateInsuranceDead=dateInsuranceDead, dateLastVisit=dateLastVisit,
                      dateNextVisit=dateNextVisit)

        db.add(tom)
        db.commit()


addPatient(surname="123", name="123", patronymic="", serial=123, number=123321, bitrh="20.12.2001",
           phoneNum="123123123", address="", workPlace="", email="", insuranceCompany="qqwe", medCardNum='123',
           dateGetted='20.12.2001', numberInsurance='123321123', dateInsuranceDead="20.12.2001", dateLastVisit="",
           dateNextVisit="")
