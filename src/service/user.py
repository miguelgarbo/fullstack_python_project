from models.schemas import *
from models.entities import *

from fastapi import HTTPException, Depends, APIRouter, Query
from http import HTTPStatus
from models.schemas import *
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database import get_session
from typing import Annotated
from service.user import *

SessionDB = Annotated[Session, Depends(get_session)]

def save(user:UserSchema):
    db_user = User(
        username=user.username,
        email=user.email,
        password=(user.password),
        role=Role.user
    )
    return db_user

def find_user_by_email(session: SessionDB, email:str):
    
    user = session.scalar(select(User).where(User.email == email))
    
    if not user:
        raise HTTPException(detail="User Not Found", status_code=404)
    
    return user

def update(id: int, user_new_data: UserSchema):
    
    ...    
    
def delete(id:int):
    ...

def find_all():
    
    return []

def find_by_id(id: int):
    return UserPublic