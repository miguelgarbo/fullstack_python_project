from fastapi.security import OAuth2PasswordBearer
from fastapi import APIRouter, Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from database import get_session, Session
from models.schemas import TokenSchema
from models.entities import User
from sqlalchemy import select
from fastapi import HTTPException
from security import verify_password, create_access_token, validate_current_user

from service.user import find_user_by_email

router = APIRouter(prefix='/login', tags=['login'])
# pelo que entendi isso vai criar um pop up de autenticação via oauth2 no swagger
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login/token')

SessionDB = Annotated[Session, Depends(get_session)]

FormData = Annotated[OAuth2PasswordRequestForm, Depends()]

Token = Annotated[str, Depends(oauth2_scheme)]


def create_dict_for_token(token: str):
    return {"access_token": token, "token_type": "Bearer"}


token = ""


@router.post('/token', response_model=TokenSchema)
def login(credentials: FormData, session: SessionDB):

    user_founded = find_user_by_email(session, credentials.username)

    if not verify_password(credentials.password, user_founded.password):
        raise HTTPException(detail="Invalid Credentials", status_code=401)

    data = {"sub": user_founded.email}

    # pega o email como assunto do token
    access_token = create_access_token(data)
    token = access_token
    print(credentials)
    return create_dict_for_token(access_token)


@router.get("/current_user")
def get_current_user(session: SessionDB, token: Token):
    print(token)
    return validate_current_user(session, token)


@router.get('/items')
def read_items(token: TokenSchema):
    return {'token': token}
