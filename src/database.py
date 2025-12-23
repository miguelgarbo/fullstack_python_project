from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models.entities import table_registry
from config import AppSettings

"""Gerenciador de Conexões, Fábrica de Conexões
   Ele sabe como conectar no banco de dados, sabe a url já
   Vai iniciar a uma sessão na função get_session abaixo"""
engine = create_engine(AppSettings().DATABASE_URL)


"""registrando tabelas no banco """
table_registry.metadata.create_all(bind=engine)

def get_session():
    with Session(engine) as session:
        yield session
