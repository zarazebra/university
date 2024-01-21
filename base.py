from sqlalchemy.orm import DeclarativeBase
from typing import List, Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True)

    professor_id: Mapped[int] = mapped_column(ForeignKey("professors.id"))
    professor: Mapped["Professor"] = relationship(back_populates="course")

    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id"))
    subject: Mapped["Subject"] = relationship(back_populates="course")

    studentrecords: Mapped["StudentRecord"] = relationship(back_populates="course")


class Professor(Base):
    __tablename__ = "professors"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]

    course: Mapped[List["Course"]] = relationship(back_populates="professor")


class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]

    studentrecords: Mapped[List["StudentRecord"]] = relationship(back_populates="student")


class StudentRecord(Base):
    __tablename__ = "studentrecords"

    id: Mapped[int] = mapped_column(primary_key=True)

    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"))
    course: Mapped[List["Course"]] = relationship(back_populates="studentrecords")

    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"))
    student: Mapped["Student"] = relationship(back_populates="studentrecords")

    grade: Mapped[int]


class Subject(Base):
    __tablename__ = "subjects"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]

    course: Mapped[List["Course"]] = relationship(back_populates="subject")
