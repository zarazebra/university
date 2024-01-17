from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import os


class DataBase:
    def __init__(self):
        engine = create_engine(os.environ.get("DATABASE_URL"), echo=True)
        self.session = Session(engine)
