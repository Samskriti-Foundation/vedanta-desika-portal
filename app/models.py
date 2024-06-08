from sqlalchemy.orm import Mapped, mapped_column
from .extensions import db


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(unique=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str]
    password: Mapped[str]
    
    def __repr__(self):
        return f"<{self.first_name} {self.last_name} | {self.email}>"


class Node(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    left: Mapped[int] = mapped_column(nullable=False)
    right: Mapped[int] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)