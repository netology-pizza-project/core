import uuid

from sqlalchemy import update

from db.base import async_session_maker
from db.models import Order, OrdersListing
from dao.base import BaseDAO


class OrderDAO(BaseDAO):
    model = Order

    @classmethod
    async def update(cls, order_id: uuid.UUID, **data):
        async with async_session_maker() as session:
            query = (
                update(cls.model)
                .where(order_id == cls.model.order_id)
                .values(**data)
                .execution_options(synchronize_session='fetch'))
            await session.execute(query)
            await session.commit()


class OrdersListingDAO(BaseDAO):
    model = OrdersListing
