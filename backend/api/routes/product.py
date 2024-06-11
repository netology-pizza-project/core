import uuid

from fastapi import APIRouter
from api.schemas.product import SProduct
from dao.product import ProductDAO

router = APIRouter()


@router.get("/", response_model=list[SProduct])
async def get_products() -> list[SProduct]:
    return await ProductDAO.get_all()


@router.get("/{id}", response_model=SProduct)
async def get_product(product_id: uuid.UUID) -> SProduct:
    return await ProductDAO.get_one_or_none(product_id=product_id)
