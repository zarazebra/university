from typing import List
from base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from course import Course


class Professor(Base):
    __tablename__ = "professors"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    courses: Mapped[List["Course"]] = relationship(back_populates="professor")

# TODO: column with birthdate?
