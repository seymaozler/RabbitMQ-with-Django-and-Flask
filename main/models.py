from sqlalchemy import Column, Integer, String, UniqueConstraint, Float
from database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True, autoincrement=False)
    title = Column(String(255), nullable=False)
    price = Column(Float, nullable=False)
    image = Column(String(255), nullable=False) 


class ProductUser(Base):
    __tablename__ = "product_user"
    id = Column(Integer, primary_key=True, index=True, autoincrement=False)
    user_id = Column(Integer, nullable=False)
    product_id = Column(Integer, nullable=False)


    