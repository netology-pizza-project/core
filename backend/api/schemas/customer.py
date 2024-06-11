import uuid

from pydantic import BaseModel


class SCustomer(BaseModel):
#    customer_id: uuid.UUID
    customer_password: str
    customer_phone: str

    class Config:
        from_attributes = True
