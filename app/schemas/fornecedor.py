from pydantic import BaseModel

class FornecedorResponse(BaseModel):
    id: int
    nome: str
    cnpj: str
    email: str
    telefone: str

    class Config:
        from_attributes = True