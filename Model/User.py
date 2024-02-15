from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    ...

class User(Base):
    __tablename__ = "user"

    login = Column(String, primary_key=True)
    password = Column(String, primary_key=True)
    personalId = Column(Integer)
    roleId = Column(Integer)