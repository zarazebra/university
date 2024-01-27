from base import Student
from database import DataBase
from sqlalchemy import select
from display import Display


class StudentRepository:
    def __init__(self):
        self.session = DataBase().get_session()

    def add_student(self, firstname, lastname):
        invalid_chars = set(".-_")
        if any((char in invalid_chars) for char in firstname):
            return print("Invalid input.")
        elif any((char in invalid_chars) for char in lastname):
            return print("Invalid input.")
        else:
            student = Student(first_name=firstname, last_name=lastname)
            self.session.add(student)
            self.session.commit()

    def edit_student(self, student_id, firstname, lastname):
        student = self.session.scalar(select(Student).where(Student.id == student_id))
        student.first_name = firstname
        student.last_name = lastname
        self.session.commit()

    def delete_student(self, student_id):
        student = self.session.scalar(select(Student).where(Student.id == student_id))
        self.session.delete(student)
        self.session.commit()

    def get_all_students(self):
        all_students = self.session.scalars(select(Student)).all()
        return all_students
