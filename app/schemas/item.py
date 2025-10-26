from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ItemBase(BaseModel):
    name: str = Field(..., description="Nome do item")
    description: Optional[str] = Field(None, description="Descrição do item")
    price: float = Field(..., ge=0, description="Preço do item")


class ItemCreate(ItemBase):
    """
    Schema para criação de item
    """
    pass


class ItemResponse(ItemBase):
    """
    Schema de resposta para item
    """
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True


class Item(ItemResponse):
    """
    Schema completo do item
    """
    pass

