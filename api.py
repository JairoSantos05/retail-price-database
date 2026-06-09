from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from dbqueries import get_prices_for_book

class Price(BaseModel):
    store: str
    price: float

class Product(BaseModel):
    isbn: str
    title: str
    prices: List[Price]
    lowest_price: float

app = FastAPI()

@app.get("/book/{isbn}/prices")
def book_prices(isbn: str):
    return get_prices_for_book(isbn)
