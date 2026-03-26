from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.produto import ProdutoCreate, ProdutoResponse
from app.services import produto_service

router = APIRouter(prefix="/produtos", tags=["Produtos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ProdutoResponse)
def criar(produto: ProdutoCreate, db: Session = Depends(get_db)):
    try:
        return produto_service.criar_produto(
            db,
            produto.nome,
            produto.descricao
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[ProdutoResponse])
def listar(db: Session = Depends(get_db)):
    return produto_service.listar_produtos(db)