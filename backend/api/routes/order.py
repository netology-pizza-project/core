import uuid

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from api.schemas.order import SOrder, SGetOrder
from dao.order import OrderDAO

router = APIRouter()


@router.get("/", response_model=SGetOrder)
async def get_order(order_id: uuid.UUID) -> SGetOrder:
    return await OrderDAO.get_by_id(order_id)


@router.post("/")
async def add_order(order_data: SOrder):
    order_id = uuid.uuid4()
    await OrderDAO.add(order_id=order_id,
                       customer_id=order_data.customer_id,
                       order_address=order_data.order_address,
                       products=order_data.products)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"order_id": str(order_id)})
