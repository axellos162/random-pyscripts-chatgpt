# Create an api using FastAPI and Pydantic that has two product classes, an empty product list,
# and an endpoint to add products to the product list which will be present in the checkout

from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float

class Checkout(BaseModel):
    products: List[Product] = []

@app.post("/checkout/add-product")
async def add_product_to_checkout(product: Product):
    checkout.products.append(product)
    return {"message": "Product added to checkout"}

@app.get("/checkout")
async def get_checkout():
    return checkout

checkout = Checkout()
