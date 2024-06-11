from db.models import Customer
from dao.base import BaseDAO


class CustomerDAO(BaseDAO):
    model = Customer
