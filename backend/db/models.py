import datetime
import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, Float, String, DateTime, Boolean, ForeignKey
from db.base import Base


class Product(Base):
    __tablename__ = 'products'

    product_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_title = Column(String, nullable=False)
    product_price = Column(Float, nullable=False)
    product_image = Column(String, nullable=False)
    product_description = Column(String, nullable=False)
    product_is_new = Column(Boolean, nullable=False, default=False)
    product_is_available = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_id = Column(UUID(as_uuid=True), ForeignKey('customers.customer_id'), nullable=False)
    order_address = Column(String, nullable=False)
    order_status = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)


class OrderListing(Base):
    __tablename__ = 'orders_listing'

    enum = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    order_id = Column(UUID(as_uuid=True), ForeignKey('orders.order_id'), default=uuid.uuid4)
    product_id = Column(UUID(as_uuid=True), ForeignKey('products.product_id'), nullable=False)
    product_quantity = Column(Integer, nullable=False)


class Cart(Base):
    __tablename__ = 'carts'

    enum = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    customer_id = Column(UUID(as_uuid=True), ForeignKey('customers.customer_id'), nullable=False)
    cart_b64_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)


class Customer(Base):
    __tablename__ = 'customers'

    customer_id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    customer_pw_hash = Column(String, nullable=False)
    customer_phone = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)

