from pydantic import BaseModel

class PedidoCreate(BaseModel):
    produto_id: int
    fornecedor_id: int
    quantidade: int