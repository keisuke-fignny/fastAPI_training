from .settings import settings           # ①で作った設定クラス
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

engine = create_async_engine(settings.database_url, echo=False, pool_pre_ping=True)
SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

async def get_session():
    async with SessionLocal() as session:
        yield session
