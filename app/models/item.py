from typing import Optional
from datetime import datetime
from app.schemas.item import Item


class ItemModel:
    def __init__(self, id: int, name: str, description: Optional[str] = None, price: float = 0.0):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.created_at = datetime.now()
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "created_at": self.created_at.isoformat()
        }

