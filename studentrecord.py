from sqlalchemy import ForeignKey
from base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from course import Course
from student import Student


class StudentRecord(Base):
    __tablename__ = "studentrecords"

    id: Mapped[int] = mapped_column(primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), unique=True)
    course: Mapped["Course"] = relationship(back_populates="studentrecords")
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"), unique=True)
    student: Mapped["Student"] = relationship(back_populates="studentrecords")
    grade: Mapped[int]
