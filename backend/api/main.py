from fastapi import APIRouter

from api.routes import product, cart, order, admin, customer
api_router = APIRouter()
# api_router.include_router(login.router, tags=["login"]) TBD
api_router.include_router(product.router, prefix="/product", tags=["product"])
api_router.include_router(cart.router, prefix="/cart", tags=["cart"])
api_router.include_router(order.router, prefix="/order", tags=["order"])
api_router.include_router(admin.router, prefix="/admin", tags=["admin"])
api_router.include_router(customer.router, prefix="/customer", tags=["customer"])
