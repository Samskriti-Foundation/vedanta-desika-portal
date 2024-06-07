from sqlalchemy.orm import Mapped, mapped_column
from .db import db


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    username: Mapped[str] = mapped_column(unique=True)