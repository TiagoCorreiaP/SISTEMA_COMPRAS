from pydantic import BaseModel
from app.schemas.produto import ProdutoResponse
from app.schemas.fornecedor import FornecedorResponse

class PedidoCreate(BaseModel):
    produto_id: int
    fornecedor_id: int
    quantidade: int
    status: str = "criado"

class PedidoResponse(BaseModel):
    id: int
    quantidade: int
    status: str

    produto: ProdutoResponse
    fornecedor: FornecedorResponse

    class Config:
        from_attributes = True