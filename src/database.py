from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from models.entities import table_registry
from config import AppSettings
import os

"""Gerenciador de Conexões, Fábrica de Conexões
   Ele sabe como conectar no banco de dados, sabe a url já
   Vai iniciar a uma sessão na função get_session abaixo"""
engine = create_engine(AppSettings().DATABASE_URL)


#só cria tabelas novas, nao atualiza mudanças
# se for atualizar, rodar no banco de dados:
# DROP DATABASE FULLSTACK_APP;
# CREATE DATABASE FULLSTACK_APP;

"""registrando tabelas no banco """
table_registry.metadata.create_all(bind=engine)
    
"""gerando arquivo dbml para documentação do dbdocs automatica"""
print("Generating dbml file")
os.system("dbdocs db2dbml postgres postgresql+psycopg://postgres:postgres@127.0.0.1:5432/fullstack_app -o database.dbml")

def get_session():
    with Session(engine) as session:
      
        yield session
