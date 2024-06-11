import uuid

from sqlalchemy import update

from db.models import Product
from dao.base import BaseDAO
from db.base import async_session_maker


class ProductDAO(BaseDAO):
    model = Product

    @classmethod
    async def update(cls, product_id: uuid.UUID, **data):
        async with async_session_maker() as session:
            query = (
                update(cls.model)
                .where(product_id == cls.model.product_id)
                .values(**data)
                .execution_options(synchronize_session='fetch'))
            await session.execute(query)
            await session.commit()
