from typing import List
from base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from course import Course


class Subject(Base):
    __tablename__ = "subjects"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]

    courses: Mapped[List["Course"]] = relationship(back_populates="subject")
