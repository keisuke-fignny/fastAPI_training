from sqlalchemy import String, Float, Integer, ARRAY
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class ItemTable(Base):
    __tablename__ = "items"

    id:    Mapped[int]        = mapped_column(Integer, primary_key=True, index=True)
    name:  Mapped[str]        = mapped_column(String(255), nullable=False)
    price: Mapped[float]      = mapped_column(Float, nullable=False)
    tags:  Mapped[list[str]]  = mapped_column(ARRAY(String), default=list)
