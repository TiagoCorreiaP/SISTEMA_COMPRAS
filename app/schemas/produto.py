from pydantic import BaseModel

class ProdutoCreate(BaseModel):
    nome: str
    descricao: str

class ProdutoResponse(BaseModel):
    id: int
    nome: str
    descricao: str

    class Config:
        from_attributes = True