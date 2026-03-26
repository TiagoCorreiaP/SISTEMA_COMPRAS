from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.produto import ProdutoCreate, ProdutoResponse
from app.services import produto_service
import app.models

router = APIRouter(prefix="/produtos", tags=["Produtos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/produtos/")
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    novo = app.models.Produto(**produto.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/", response_model=list[ProdutoResponse])
def listar(db: Session = Depends(get_db)):
    return produto_service.listar_produtos(db)