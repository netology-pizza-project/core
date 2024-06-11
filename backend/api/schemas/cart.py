import uuid

from pydantic import BaseModel


class SCart(BaseModel):
    customer_id: uuid.UUID
    cart_b64_hash: str

    class Config:
        from_attributes = True


class SGetCart(BaseModel):
    cart_b64_hash: str

    class Config:
        from_attributes = True
