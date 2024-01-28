from base import Course
from database import DataBase
from sqlalchemy import select


class CourseRepository:
    def __init__(self):
        self.session = DataBase().get_session()

    def get_all_courses(self):
        all_courses_data = select(Course).join(Course.professor).join(Course.subject)
        all_courses = self.session.scalars(all_courses_data).all()
        return all_courses

    def add_course(self, professor_id, subject_id):
        new_course = Course(professor_id=professor_id, subject_id=subject_id)
        self.session.add(new_course)
        self.session.commit()

    def edit_course(self, course_id, new_professor_id, new_subject_id):
        course = self.session.scalar(select(Course).where(Course.id == course_id))
        if new_professor_id:
            course.professor_id = new_professor_id
        if new_subject_id:
            course.subject_id = new_subject_id
        self.session.commit()

    def delete_course(self, course_id):
        course = self.session.scalar(select(Course).where(Course.id == course_id))
        self.session.delete(course)
        self.session.commit()
