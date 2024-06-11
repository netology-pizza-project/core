from sqlalchemy.dialects.postgresql import insert

from db.base import async_session_maker
from db.models import Order, OrderListing
from dao.base import BaseDAO


class OrderDAO(BaseDAO):
    model = Order

    listing_model = OrderListing

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(customer_id=data['customer_id'],
                                             order_address=data['order_address'],
                                             order_status="created")
            await session.execute(query)
            await session.commit()
            query = insert(cls.listing_model).values(data['products'])
            await session.execute(query)
            await session.commit()
