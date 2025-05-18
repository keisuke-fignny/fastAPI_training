from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession, async_sessionmaker, create_async_engine,
)

DATABASE_URL = "postgresql+asyncpg://ユーザ名:パスワード@localhost:5432/データベース名"

engine = create_async_engine(
    DATABASE_URL,
    echo=True,            # SQL ログを出すなら True
    pool_pre_ping=True   # 死活監視で接続切れを検知
)
SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session
