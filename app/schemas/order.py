from pydantic import BaseModel
from typing import Optional


class OrderCreate(BaseModel):
    user_id: int
    product_name: str
    quantity: int
    price: float
class OrderUpdate(BaseModel):
    product_name: Optional[str] = None
    quantity: Optional[int] = None

class OrderResponse(BaseModel):
    order_id: int
    user_id: int
    product_name: str
    quantity: int
    price: float
    status: str