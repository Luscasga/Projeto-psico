from fastapi import FastAPI
from routes import auth, pacientes, consultas
from database.db import init_db

app = FastAPI()

# Inicializar o banco de dados
init_db()

# Incluir rotas
app.include_router(auth.router, prefix="/auth", tags=["Autenticação"])
app.include_router(pacientes.router, prefix="/pacientes", tags=["Pacientes"])
app.include_router(consultas.router, prefix="/consultas", tags=["Consultas"])
