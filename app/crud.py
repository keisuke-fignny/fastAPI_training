from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound
from typing import List

from .models import ItemTable
from .schemas import ItemCreate, Item


# --------- items データ作成 ---------
async def create_item(db: AsyncSession, data: ItemCreate) -> Item:
    record = ItemTable(**data.model_dump())
    db.add(record)
    await db.commit()
    await db.refresh(record)
    return Item.model_validate(record)

# ---------- items ID指定で1レコード取得
async def get_item(db: AsyncSession, item_id: int) -> Item:
    stmt = select(ItemTable).where(ItemTable.id == item_id)
    try:
        result = await db.execute(stmt)
        record = result.scalar_one()
    except NoResultFound:
        return None
    return Item.model_validate(record)

# ---------- items 一覧 ----------
async def list_items(db: AsyncSession) -> List[Item]:
    stmt = select(ItemTable).order_by(ItemTable.id)
    res = await db.execute(stmt)
    rows = res.scalars().all()
    return [Item.model_validate(r) for r in rows]
