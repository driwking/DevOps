from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import json

app = FastAPI()

def load_data():
    with open("mock.json", "r", encoding="utf-8") as f:
        return json.load(f)

class Item(BaseModel):
    id: int
    item: str
    price: str | None = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items",response_model=List[Item])
def get_items():
    return load_data()


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = next((i for i in load_data() if i['id'] == item_id),None)
    if not item:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return item