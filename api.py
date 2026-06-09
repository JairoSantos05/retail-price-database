from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class Price(BaseModel):
    store: str
    price: float

class Product(BaseModel):
    isbn: str
    title: str
    prices: List[Price]
    lowest_price: float

app = FastAPI()

@app.get("/products")
def get_products():
    return get_all_products()

@app.get("/products/{isbn}")
def get_product(isbn: str):
    return get_product(isbn)
