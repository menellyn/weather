from sqlalchemy.orm import Mapped, mapped_column

from app.api.dao.database import Base

class UsersOrm(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    login: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]

