from pydantic import BaseModel

class ProductBase(BaseModel):
    id: int
    title: str
    price: float
    image: str

    class Config:
        orm_mode = True

class ProductUser(BaseModel):
    id: int
    user_id: int
    product_id: int

    class Config:
        orm_mode = True