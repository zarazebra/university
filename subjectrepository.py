from base import Subject
from database import DataBase
from sqlalchemy import select


class SubjectRepository:
    def __init__(self):
        self.session = DataBase().get_session()

    def add_subject(self, title):
        invalid_chars = set(".-_")
        if any((char in invalid_chars) for char in title):
            return print("Invalid input.")
        else:
            new_subject = Subject(title=title)
            self.session.add(new_subject)
            self.session.commit()

    def edit_subject(self, subject_id, new_title):
        subject = self.session.scalar(select(Subject).where(Subject.id == subject_id))
        subject.title = new_title
        self.session.commit()

    def delete_subject(self, subject_id):
        subject = self.session.scalar(select(Subject).where(Subject.id == subject_id))
        self.session.delete(subject)
        self.session.commit()

    def get_all_subjects(self):
        all_subjects = self.session.scalars(select(Subject)).all()
        return all_subjects
