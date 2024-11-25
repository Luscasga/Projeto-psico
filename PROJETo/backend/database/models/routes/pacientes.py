from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import SessionLocal
from models.paciente import Paciente

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def criar_paciente(nome: str, idade: int, endereco: str, db: Session = Depends(get_db)):
    paciente = Paciente(nome=nome, idade=idade, endereco=endereco)
    db.add(paciente)
    db.commit()
    return {"message": "Paciente criado com sucesso"}

@router.get("/")
def listar_pacientes(db: Session = Depends(get_db)):
    return db.query(Paciente).all()
