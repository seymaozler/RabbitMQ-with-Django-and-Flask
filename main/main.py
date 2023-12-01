from fastapi import FastAPI
from models import Product
from database import db
from schemas import ProductBase
from producer import publish
import requests


app = FastAPI()

@app.get("/api/products")
async def root():
    products = db.query(Product).all()
    return products


@app.post("/api/products/{product_id}/like")
async def like_product(product_id: int):
    req = requests.get("http://host.docker.internal:8000/api/user")
    data = req.json()

    try:
        product_user = ProductBase(user_id=data['id'], product_id=product_id)
        db.add(product_user)
        db.commit()

        publish('product_liked', product_id)
        return {"message": "success"}
    except:
        return {"message": "You already liked this product"}
