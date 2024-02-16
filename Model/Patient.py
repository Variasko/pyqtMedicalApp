from typing import Type

from sqlalchemy import Column, String, Integer, DateTime, Date
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    ...

class Patient(Base):
    __tablename__ = 'patient'

    id = Column(Integer, primary_key=True, index=True)
    surname = Column(String)
    name = Column(String)
    patronymic = Column(String)
    pasportSerial = Column(Integer)
    pasportNumber = Column(Integer)
    birthday = Column(String)
    genderId = Column(Integer)
    address = Column(String)
    contactPhoneNumber = Column(String)
    email = Column(String)
    numberMedicalCard = Column(Integer)
    dateGetMedicalCard = Column(String)
    dateLastVisit = Column(String)
    dateNextVisit = Column(String)
    numberInsurancePolicy = Column(Integer)
    dateOfDeadIncurancePolicy = Column(String)
    workingPlace = Column(String)
    InsuranceCompany = Column(String)



