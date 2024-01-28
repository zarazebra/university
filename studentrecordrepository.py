from base import StudentRecord
from database import DataBase
from sqlalchemy import select


class StudentRecordRepository:
    def __init__(self):
        self.session = DataBase().get_session()

    def get_all_studentrecords(self):
        all_studentrecords_data = select(StudentRecord).join(StudentRecord.course).join(StudentRecord.student)
        all_studentrecords = self.session.scalars(all_studentrecords_data).all()
        return all_studentrecords

    def add_studentrecord(self, student_id, course_id):
        new_studentrecord = StudentRecord(student_id=student_id, course_id=course_id)
        self.session.add(new_studentrecord)
        self.session.commit()

    def submit_grade(self, studentrecord_id, new_grade):
        studentrecord = self.session.scalar(select(StudentRecord).where(StudentRecord.id == studentrecord_id))
        studentrecord.grade = new_grade
        self.session.commit()

    def delete_studentrecord(self, studentrecord_id):
        studentrecord = self.session.scalar(select(StudentRecord).where(StudentRecord.id == studentrecord_id))
        self.session.delete(studentrecord)
        self.session.commit()
