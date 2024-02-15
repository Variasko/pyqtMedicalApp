from sqlalchemy import *
from psycopg2 import *
from sqlalchemy.orm import Session
from Model.User import *

postgresqlDB = "postgresql://postgres:1@127.0.0.1:5433/MedicalDatabase"

engine = create_engine(postgresqlDB, echo=True)

def validatePerson(login, password):
    with Session(autoflush=False, bind=engine) as db:
        users = db.query(User).all()

        isLoggined = False


        for i in users:
            if (i.login == login and i.password == password):
                return True

    print(1)


