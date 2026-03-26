from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import SessionLocal
import app.models as models
from app.core.auth import hash_senha, verificar_senha, criar_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UsuarioCreate(BaseModel):
    username: str
    senha: str

@router.post("/usuarios/")
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    novo = models.Usuario(
        username=usuario.username,
        senha=hash_senha(usuario.senha)
    )
    db.add(novo)
    db.commit()
    return {"msg": "Usuário criado"}

class Login(BaseModel):
    username: str
    senha: str

@router.post("/login")
def login(dados: Login, db: Session = Depends(get_db)):
    user = db.query(models.Usuario).filter(
        models.Usuario.username == dados.username
    ).first()

    if not user or not verificar_senha(dados.senha, user.senha):
        return {"erro": "Credenciais inválidas"}

    token = criar_token({"sub": user.username})
    return {"access_token": token}