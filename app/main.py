from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from .database import engine, get_session
from .models import Base
from .schemas import ItemCreate, Item
from . import crud

app = FastAPI(title="FastAPI + PostgreSQL (split files)")

@app.get("/")
def root():
    return {"hello": "world"}

# ---------- items 作成エンドポイント----------
@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(
    item: ItemCreate,
    db: AsyncSession = Depends(get_session),
):
    return await crud.create_item(db, item)

# ---------- items 1アイテム取得エンドポイント ----------
@app.get("/items/{item_id}", response_model=Item)
async def read_item(
    item_id: int,
    db: AsyncSession = Depends(get_session),
):
    record = await crud.get_item(db, item_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return record

# ---------- tems 一覧エンドポイント ----------
@app.get("/items/", response_model=list[Item])
async def list_items(
    db: AsyncSession = Depends(get_session),
):
    return await crud.list_items(db)
