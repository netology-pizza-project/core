import uuid

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from api.schemas.cart import SCart, SGetCart
from dao.cart import CartDAO

router = APIRouter()


@router.get("/", response_model=SGetCart)
async def get_cart(customer_id: uuid.UUID) -> SCart:
    return await CartDAO.get_by_id(customer_id)


@router.post("/")
async def add_cart(cart_data: SCart):
    cart_id = uuid.uuid4()
    await CartDAO.add(cart_id=cart_id,
                      customer_id=cart_data.customer_id,
                      cart_b64_hash=cart_data.cart_b64_hash)
    return JSONResponse(status_code=status.HTTP_201_CREATED,
                        content={"cart_id": str(cart_id)})
