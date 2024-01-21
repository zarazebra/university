from base import Student
from database import DataBase
from sqlalchemy import select


class StudentService:
    def __init__(self):
        self.session = DataBase().get_session()

    def add_student(self, firstname, lastname):
        student = Student(first_name=firstname, last_name=lastname)
        self.session.add(student)
        self.session.commit()

    def edit_student(self, student_id, firstname, lastname):
        student = self.session.scalar(select(Student).where(Student.id == student_id))
        student.first_name = firstname
        student.last_name = lastname
        self.session.commit()

    def delete_student(self):
        pass

    def get_all_students(self):
        pass
