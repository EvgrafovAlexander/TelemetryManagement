# thirdparty
from pydantic import BaseModel
from sqlalchemy import exc
from sqlalchemy.ext.asyncio import AsyncSession

# project
from src.database import Base
from src.utils.exceptions import DatabaseError


class BaseRepository:
    model = Base

    def __init__(self, session: AsyncSession):
        self.session = session

    def _create_alchemy_model(self, pydantic_model: BaseModel):
        return self.model(**pydantic_model.dict())

    async def _commit(self):
        try:
            await self.session.commit()
        except exc.SQLAlchemyError as e:
            await self.session.rollback()
            raise DatabaseError(e.orig)
        except ConnectionRefusedError as e:
            raise DatabaseError(e)
        except Exception:
            raise
