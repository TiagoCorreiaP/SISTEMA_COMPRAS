from pydantic import BaseModel

class ProdutoCreate(BaseModel):
    nome: str
    descricao: str
    preco: float

class ProdutoResponse(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float

    class Config:
        from_attributes = True