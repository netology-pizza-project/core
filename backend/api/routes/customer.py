import uuid

from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse

from api.schemas.customer import SCustomer
from dao.customer import CustomerDAO

router = APIRouter()


@router.post("/")
async def add_customer(customer_data: SCustomer):
    customer_id = uuid.uuid4()
    customer_pw_hash = str(hash(customer_data.customer_password))
    db_item = await CustomerDAO.get_one_or_none(customer_phone=customer_data.customer_phone)
    if db_item:
        raise HTTPException(status_code=500, detail="User with this phone number already exists")
    await CustomerDAO.add(customer_id=customer_id,
                          customer_pw_hash=customer_pw_hash,
                          customer_phone=customer_data.customer_phone)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"customer_id": str(customer_id)})
