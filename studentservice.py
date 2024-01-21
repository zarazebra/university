from base import *
from database import DataBase


class StudentService:
    def __init__(self):
        self.session = DataBase().get_session()

    def add_student(self, firstname, lastname):
        student = Student(first_name=firstname, last_name=lastname)
        self.session.add(student)
        self.session.commit()

    def edit_student(self):
        pass

    def delete_student(self):
        pass

    def get_all_students(self):
        pass
