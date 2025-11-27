from fastapi import FastAPI
from pydantic import BaseModel
from app.api.items import router as items_router

""" app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hola Cloud Developer!"}

# Modelo de datos que recibirá el endpoint POST
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

@app.post("/items")
def create_item(item: Item):
    return {
        "msg": "Item recibido correctamente",
        "data": item
    } """


app = FastAPI(
    title="CRUD Training API",
    version="1.0.0"
)

app.include_router(items_router)