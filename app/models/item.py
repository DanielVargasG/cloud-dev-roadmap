from pydantic import BaseModel, Field, conint, constr
from typing import Optional

class ItemBase(BaseModel):
    name: constr(min_length=3, max_length=50)
    price: conint(gt=0)  # precio debe ser > 0
    description: Optional[str] = Field(None, max_length=255)

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
