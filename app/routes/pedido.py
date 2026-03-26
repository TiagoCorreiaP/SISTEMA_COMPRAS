from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import SessionLocal
import app.models as models

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ProdutoCreate(BaseModel):
    nome: str
    descricao: str

@router.post("/produtos/")
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    novo = models.Produto(**produto.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/produtos/")
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(models.Produto).all()