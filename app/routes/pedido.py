from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.pedido import PedidoCreate, PedidoResponse
from app.services import pedido_service

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def criar(pedido: PedidoCreate, db: Session = Depends(get_db)):
    return pedido_service.criar_pedido(db, pedido)

@router.get("/", response_model=list[PedidoResponse])
def listar(db: Session = Depends(get_db)):
    return pedido_service.listar_pedidos(db)