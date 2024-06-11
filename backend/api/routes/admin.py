import uuid

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from dao.product import ProductDAO
from api.schemas.product import SAddProduct
from api.schemas.order import SOrder

router = APIRouter()

# @router.get("/", response_model=GetCart)
# async def get_cart(customer_id: uuid.UUID):
#     return await CartDAO.get_by_id(customer_id)()


@router.post("/product")
async def add_product(product_data: SAddProduct):
    product_id = uuid.uuid4()
    await ProductDAO.add(product_id=product_id,
                         product_title=product_data.product_title,
                         product_price=product_data.product_price,
                         product_description=product_data.product_description,
                         product_image=product_data.product_image,
                         product_is_new=product_data.product_is_new,
                         product_is_available=product_data.product_is_available)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"product_id": str(product_id)})


@router.put("/product", response_model=SProduct)
async def update_product(product_data: SProduct):
    db_item = await ProductDAO.get_by_id(product_data.product_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return await ProductDAO.update(product_id=db_item.product_id,
                                   product_title=product_data.product_title,
                                   product_price=product_data.product_price,
                                   product_description=product_data.product_description,
                                   product_image=product_data.product_image,
                                   product_is_new=product_data.product_is_new,
                                   product_is_available=product_data.product_is_available)


@router.put("/order", response_model=SOrder)
async def update_order(order_data: SOrder):
    db_item = await ProductDAO.get_by_id(order_data.order_id)
    if db_item is None:
        raise HTTPException(status_code=500, detail="Order not found")
    return await ProductDAO.update(order_status=order_data.order_status)
