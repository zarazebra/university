from typing import List
from sqlalchemy import ForeignKey
from base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from professor import Professor
from studentrecord import StudentRecord
from subject import Subject


class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)

    professor_id: Mapped[int] = mapped_column(ForeignKey("professors.id"))
    professor: Mapped["Professor"] = relationship(back_populates="courses")
    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id"))
    subject: Mapped["Subject"] = relationship(back_populates="courses")

    studentrecords: Mapped[List["StudentRecord"]] = relationship(back_populates="courses")
