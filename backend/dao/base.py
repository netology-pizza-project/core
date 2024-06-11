import uuid

from db.base import async_session_maker
from sqlalchemy import select, insert, update


class BaseDAO:

    model = None

    @classmethod
    async def get_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            products = result.scalars().one_or_none()
            if products is None:
                return False
            return products.__dict__

    @classmethod
    async def get_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model)
            result = await session.execute(query)
            products = result.scalars().all()
            return [product.__dict__ for product in products]

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update(cls, **data):
        async with async_session_maker() as session:
            query = update(cls.model).values(**data)
            await session.execute(query)
            await session.commit()
