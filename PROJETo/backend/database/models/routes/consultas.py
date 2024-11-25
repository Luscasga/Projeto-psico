from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.db import SessionLocal
from models.consulta import Consulta

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def criar_consulta(paciente_id: int, data_horario: str, db: Session = Depends(get_db)):
    consulta = Consulta(paciente_id=paciente_id, data_horario=data_horario)
    db.add(consulta)
    db.commit()
    return {"message": "Consulta criada"}

@router.get("/")
def listar_consultas(db: Session = Depends(get_db)):
    return db.query(Consulta).all()
