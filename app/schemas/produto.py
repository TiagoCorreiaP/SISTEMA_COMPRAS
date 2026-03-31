from pydantic import BaseModel
from typing import Optional

class ProdutoCreate(BaseModel):
    nome: str
    descricao: str
    preco: float

class ProdutoResponse(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: Optional[float]

    class Config:
        from_attributes = True

        