from fastapi import APIRouter
from app.models.item import Item, ItemCreate

router = APIRouter(prefix="/items", tags=["Items"])

# Simulación temporal en memoria
DB = []


@router.post("/", response_model=Item)
def create_item(item: ItemCreate):
    # Convert ItemCreate to Item and add ID
    new_item = Item(**item.model_dump(), id=len(DB) + 1)
    DB.append(new_item)
    return new_item


@router.get("/", response_model=list[Item])
def list_items():
    return DB


@router.get("/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in DB:
        if item.id == item_id:
            return item
    return {"error": "Item not found"}


@router.put("/{item_id}", response_model=Item)
def update_item(item_id: int, data: ItemCreate):
    for index, item in enumerate(DB):
        if item.id == item_id:
            # Convert ItemCreate to Item and preserve ID
            updated_item = Item(**data.model_dump(), id=item_id)
            DB[index] = updated_item
            return updated_item
    return {"error": "Item not found"}


@router.delete("/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(DB):
        if item.id == item_id:
            DB.pop(index)
            return {"message": "Item deleted"}
    return {"error": "Item not found"}
