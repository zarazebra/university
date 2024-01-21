from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv
from base import Base

load_dotenv()


class DataBase:
    def __init__(self):
        self.engine = create_engine(os.environ["DATABASE_CONNECTION_STRING"], echo=True)
        Base.metadata.create_all(self.engine)

    def get_session(self):
        session = Session(self.engine)
        return session
