from pydantic import EmailStr, BaseModel
from typing import Optional
from enum import Enum


class Role(str,Enum):
    admin = 'ADMIN'
    user = 'USER'
    

class UserSchema(BaseModel):
    name: str
    password: str
    email: EmailStr
    
class UserSchemaUpdate(BaseModel):
    name: str
    email: EmailStr
    
class UserPublic(BaseModel):
    name: str
    email: EmailStr
    role: Role


class UserPublicList(BaseModel):
    users: list[UserPublic]
    
    
class TokenSchema(BaseModel):
    access_token: str  # O Token jwt que vamos gerar
    token_type: str  # O Modelo que o cliente deve usar para a autorização
