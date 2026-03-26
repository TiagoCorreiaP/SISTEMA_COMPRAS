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

class FornecedorCreate(BaseModel):
    nome: str
    cnpj: str
    email: str
    telefone: str

@router.post("/fornecedores/")
def criar_fornecedor(fornecedor: FornecedorCreate, db: Session = Depends(get_db)):
    novo = models.Fornecedor(**fornecedor.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/fornecedores/")
def listar_fornecedores(db: Session = Depends(get_db)):
    return db.query(models.Fornecedor).all()