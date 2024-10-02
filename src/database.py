# stdlib
from collections.abc import AsyncGenerator

# thirdparty
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.ext.declarative import declarative_base

# project
from src.config import db_config


engine = create_async_engine(db_config.url)
async_session = async_sessionmaker(engine)

# Model base class
Base = declarative_base()


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


class CustomBase(Base):
    __abstract__ = True
    __table_args__ = {"extend_existing": True}
