from base import Professor
from database import DataBase
from sqlalchemy import select


class ProfessorRepository:
    def __init__(self):
        self.session = DataBase().get_session()

    def add_professor(self, firstname, lastname):
        invalid_chars = set(".-_")
        if any((char in invalid_chars) for char in firstname):
            return print("Invalid input.")
        elif any((char in invalid_chars) for char in lastname):
            return print("Invalid input.")
        else:
            professor = Professor(first_name=firstname, last_name=lastname)
            self.session.add(professor)
            self.session.commit()

    def edit_professor(self, professor_id, firstname, lastname):
        professor = self.session.scalar(select(Professor).where(Professor.id == professor_id))
        professor.first_name = firstname
        professor.last_name = lastname
        self.session.commit()

    def delete_professor(self, professor_id):
        professor = self.session.scalar(select(Professor).where(Professor.id == professor_id))
        self.session.delete(professor)
        self.session.commit()

    def get_all_professors(self):
        all_professors = self.session.scalars(select(Professor)).all()
        return all_professors
