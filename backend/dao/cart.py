from db.models import Cart
from dao.base import BaseDAO


class CartDAO(BaseDAO):
    model = Cart
