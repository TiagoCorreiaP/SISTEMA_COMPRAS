from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.pedido import PedidoCreate
from app.services import pedido_service

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def criar_pedido(pedido: PedidoCreate, db: Session = Depends(get_db)):
    return pedido_service.criar_pedido(
        db,
        pedido.produto_id,
        pedido.fornecedor_id,
        pedido.quantidade
    )