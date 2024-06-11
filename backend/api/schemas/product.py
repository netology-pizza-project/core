import uuid

from pydantic import BaseModel


class SProduct(BaseModel):
    product_id: uuid.UUID
    product_title: str
    product_price: float
    product_image: str
    product_description: str
    product_is_new: bool
    product_is_available: bool

    class Config:
        from_attributes = True


class SAddProduct(BaseModel):
    product_title: str
    product_price: float
    product_image: str
    product_description: str
    product_is_new: bool
    product_is_available: bool

    class Config:
        from_attributes = True
