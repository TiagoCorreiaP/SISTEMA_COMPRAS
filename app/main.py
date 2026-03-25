from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
import models
from core.auth import hash_senha, verificar_senha, criar_token, jwt, SECRET_KEY, ALGORITHM
from fastapi.security import OAuth2PasswordBearer
from core.auth import get_usuario_logado
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

usuario_logado = Depends(get_usuario_logado)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from pydantic import BaseModel

class FornecedorCreate(BaseModel):
    nome: str
    cnpj: str
    email: str
    telefone: str

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_usuario_logado(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401)
        return username
    except:
        raise HTTPException(status_code=401)
    
@app.post("/fornecedores/")
def criar_fornecedor(fornecedor: FornecedorCreate, db: Session = Depends(get_db)):
    novo = models.Fornecedor(**fornecedor.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


@app.get("/fornecedores/")
def listar_fornecedores(db: Session = Depends(get_db)):
    return db.query(models.Fornecedor).all()

class ProdutoCreate(BaseModel):
    nome: str
    descricao: str


@app.post("/produtos/")
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    novo = models.Produto(**produto.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


@app.get("/produtos/")
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(models.Produto).all()

class PedidoCreate(BaseModel):
    produto_id: int
    fornecedor_id: int
    quantidade: int
    status: str


@app.post("/pedidos/")
def criar_pedido(pedido: PedidoCreate, db: Session = Depends(get_db)):
    novo = models.Pedido(**pedido.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


@app.get("/pedidos/")
def listar_pedidos(db: Session = Depends(get_db)):
    return db.query(models.Pedido).all()

class UsuarioCreate(BaseModel):
    username: str
    senha: str

@app.post("/usuarios/")
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

@app.post("/login")
def login(dados: Login, db: Session = Depends(get_db)):
    user = db.query(models.Usuario).filter(
        models.Usuario.username == dados.username
    ).first()

    if not user or not verificar_senha(dados.senha, user.senha):
        return {"erro": "Credenciais inválidas"}

    token = criar_token({"sub": user.username})
    return {"access_token": token}