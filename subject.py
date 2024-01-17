from base import Base
from sqlalchemy.orm import Mapped, mapped_column


class Subject(Base):
    __tablename__ = "subjects"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
