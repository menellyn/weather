from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from decimal import Decimal

from app.api.dao.database import Base

class LocationsOrm(Base):
    __tablename__ = "locations"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] 
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    latitude: Mapped[Decimal]
    longitude: Mapped[Decimal]

