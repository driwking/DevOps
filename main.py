from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

mock_items = [
    {"id": 1, "item": "café 1kg", "price": "14.00"},
    {"id": 2, "item": "macarrão 300g", "price": "3.50"},
    {"id": 3, "item": "Feijao 1kg", "price": "5.20"}
]

class Item(BaseModel):
    id: int
    item: str
    price: str | None = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items",response_model=List[Item])
def get_items():
    return mock_items


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = next((i for i in mock_items if i['id'] == item_id),None)
    if not item:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return item
    

