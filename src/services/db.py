from sqlmodel.ext.asyncio.session import AsyncSession

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine

from core.config import database_config, app_config


DATABASE_URL = database_config.database_url

engine = create_async_engine(DATABASE_URL, echo=app_config.debug)


async def get_session() -> AsyncSession:
    session = sessionmaker(  # noqa
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )
    async with session() as session:
        yield session
