from base import Base
from sqlalchemy.orm import Mapped, mapped_column


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]

# TODO: column with birthdate
