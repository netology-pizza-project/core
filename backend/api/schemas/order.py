import uuid
from typing import List

from pydantic import BaseModel


class SOrderValues(BaseModel):
    product_id: uuid.UUID
    product_quantity: int


class SOrder(BaseModel):
    customer_id: uuid.UUID
    order_address: str
    products: List[SOrderValues]

    class Config:
        from_attributes = True


class SGetOrder(BaseModel):
    order_status: str

    class Config:
        from_attributes = True


class SUpdateOrder(BaseModel):
    order_id: uuid.UUID
    order_status: str

    class Config:
        from_attributes = True
