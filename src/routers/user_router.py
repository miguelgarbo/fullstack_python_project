from fastapi import HTTPException, Depends, APIRouter, Query
from http import HTTPStatus
from models.schemas import UserSchema, UserPublic
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database import get_session
from typing import Annotated
from service.user_service import *

router_user = APIRouter(prefix='/users', tags=['users'])

SessionDB = Annotated[Session, Depends(get_session)]


@router_user.post(
    '/save', response_model=UserPublic, status_code=HTTPStatus.CREATED
)
def create_user(user_new: UserSchema, session: SessionDB):

    exist_user_credentials = session.scalar(select(User)
                                            .where( (User.name == user_new.name) | 
                                            (User.email == user_new.email))
                                           )
    
    if exist_user_credentials:
        if(exist_user_credentials.name == user_new.name):
            raise HTTPException(detail='This Name Already Exists in DataBase',
                                status_code=HTTPStatus.CONFLICT)
        
        if(exist_user_credentials.email == user_new.email):
            raise HTTPException(detail='This Email Already Exists in DataBase',
                                status_code=HTTPStatus.CONFLICT)
        
        
    db_user = User(
        name=user_new.name,
        email=user_new.email,
        password=(user_new.password),
        role=Role.user
    )
    
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    
    return db_user
    
@router_user.get('/', response_model=None, status_code=HTTPStatus.OK)
async def read_users(
    session: SessionDB,
):
    users = session.scalars(select(User))

    return {'users': users}
    

