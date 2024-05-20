from typing import List, Union

import database
import model
from fastapi import Depends, FastAPI, HTTPException
from schema import Item, ItemBase, ItemCreate
from sqlalchemy.orm import session

app = FastAPI()

model.Base.metadata.create_all(bind=database.engine)


@app.get("/")
def init():
    return {"message": "Hello World"}


@app.post("/items/", response_model=Item)
def create_item(item: ItemCreate, db: session = Depends(database.get_db)):
    db_item = model.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.get("/items/", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 10, db: session = Depends(database.get_db)):
    items = db.query(model.Item).offset(skip).limit(limit).all()
    return items


@app.put("/items/{item_id}", response_model=Item)
def update_items(
    item_id: int, item: ItemCreate, db: session = Depends(database.get_db)
):
    db_item = db.query(model.Item).filter(model.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in item:
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.delete("/items/{item_id}", response_model=Item)
def delete_items(item_id: int, db: session = Depends(database.get_db)):
    db_item = db.query(model.Item).filter(model.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return db_item
