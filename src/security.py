from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from typing import Annotated
from database import get_session
from sqlalchemy.orm import Session
from pwdlib import PasswordHash
from datetime import datetime, UTC, timedelta
from config import settings
from jwt import encode, decode, DecodeError, ExpiredSignatureError
from service.user import find_user_by_email

# Criação do contexo da criptografia
# Esse pwd é uma biblioteca que usa algoritmos de geração de hashs

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login/token')

pwd_context = PasswordHash.recommended()
Token = Annotated[str, Depends(oauth2_scheme)]
SessionDB = Annotated[Session, Depends(get_session)]


def generate_password_hash(password: str):
    return pwd_context.hash(password)

# essa função pega a senha limpa , ele vai encriptar a senha 
# ver se bate com a do banco armazenada

def verify_password(clean_password: str, hashed_password: str): 
    return pwd_context.verify(clean_password, hashed_password)
    
#função para validar se o usuario tem um token na header
def validate_current_user(session: SessionDB, token: Token):
    
    #decodificando o token com secret key e algoritmo de desencriptação
    payload = decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    
    email: str = payload.get("sub")
    
    if email is None:
        raise DecodeError("Could not validate credentials")
    
    current_user = find_user_by_email(session, email)

    return current_user
    
def create_access_token(data:dict):
    
    to_encode = data.copy()
    
    expire = datetime.now(UTC) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    
    #criando o corpo do token com aqueles hashs e pontos do JWT
    encode_jwt = encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    
    return encode_jwt