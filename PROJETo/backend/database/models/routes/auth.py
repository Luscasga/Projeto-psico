from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt
from database.db import SessionLocal
from models.medico import Medico
from datetime import datetime, timedelta

SECRET_KEY = "sua_chave_secreta"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def registrar_medico(nome: str, email: str, senha: str, db: Session = Depends(get_db)):
    hashed_senha = pwd_context.hash(senha)
    novo_medico = Medico(nome=nome, email=email, senha=hashed_senha)
    db.add(novo_medico)
    db.commit()
    return {"message": "Médico registrado"}

@router.post("/login")
def login(email: str, senha: str, db: Session = Depends(get_db)):
    medico = db.query(Medico).filter(Medico.email == email).first()
    if not medico or not pwd_context.verify(senha, medico.senha):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = jwt.encode({"sub": email, "exp": datetime.utcnow() + timedelta(minutes=30)}, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token}
