from sqlalchemy import Column, Integer, String, ForeignKey
from database.db import Base

class Consulta(Base):
    __tablename__ = "consultas"

    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"))
    data_horario = Column(String)
