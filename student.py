from typing import List
from base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from studentrecord import StudentRecord


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]

    studentrecords: Mapped[List["StudentRecord"]] = relationship(back_populates="students")
