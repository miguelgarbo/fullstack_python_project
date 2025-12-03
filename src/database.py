from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models.entities import table_registry
from config import AppSettings

engine = create_engine(AppSettings().DATABASE_URL)

table_registry.metadata.create_all(bind=engine)

def get_session():
    with Session(engine) as session:
        yield session
