from typing import List
from pydantic import BaseModel, Field

class ItemCreate(BaseModel):
    name:  str        = Field(..., example="Banana")
    price: float      = Field(..., ge=0, example=1.5)
    tags:  List[str]  = Field(default_factory=list, example=["fruit", "yellow"])

class Item(ItemCreate):
    id: int

    class Config:
        from_attributes = True   # SQLAlchemy → Pydantic 自動変換
