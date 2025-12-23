from fastapi import HTTPException, Depends, APIRouter, Query
from http import HTTPStatus
from models.schemas import UserSchema, UserPublic, UserSchemaUpdate
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from database import get_session
from typing import Annotated
from service.user import *
from security import validate_current_user, generate_password_hash


router = APIRouter(prefix='/users', tags=['users'])

CurrentUser = Annotated[User, Depends(validate_current_user)]

SessionDB = Annotated[Session, Depends(get_session)]  # type: ignore


@router.post(
    '/save', response_model=UserPublic, status_code=HTTPStatus.CREATED
)
def create_user(user_new: UserSchema, session: SessionDB):  # type: ignore

    already_exists(user_new, session)
    # travando se já existir o usuario com as msms credenciais

    db_user = User(
        name=user_new.name,
        email=user_new.email,
        password=generate_password_hash(user_new.password),
        role=Role.user
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


def already_exists(user_new, session: Session) -> bool:  # type: ignore

    exist_user_credentials = session.scalar(select(User)
                                            .where((User.name == user_new.name) |
                                            (User.email == user_new.email))
                                            )

    if exist_user_credentials:
        if (exist_user_credentials.name == user_new.name):
            raise HTTPException(detail='This Name Already Exists in DataBase',
                                status_code=HTTPStatus.CONFLICT)

        if (exist_user_credentials.email == user_new.email):
            raise HTTPException(detail='This Email Already Exists in DataBase',
                                status_code=HTTPStatus.CONFLICT)
        return True

    return False


@router.get("/findById/{user_id}", response_model=UserPublic, status_code=HTTPStatus.OK)
def read_user_by_id(session: SessionDB, user_id: int):  # type: ignore
    user_founded = session.scalar(select(User).where(User.id == user_id))

    if not user_founded:
        raise HTTPException(detail="User Not Found",
                            status_code=HTTPStatus.NOT_FOUND)

    return user_founded


@router.put("/update/{user_id}", response_model=UserPublic, status_code=HTTPStatus.OK)
def update_user(session: SessionDB, user_id: int, user_new_data: UserSchemaUpdate, currrent_user: CurrentUser):  # type: ignore

    already_exists(user_new_data, session)
    # travando se já existir o usuario com as msms credenciais

    user_founded = read_user_by_id(session, user_id)

    user_founded.name = user_new_data.name
    user_founded.email = user_new_data.email
    user_founded.password = user_founded.password

    session.commit()
    session.refresh(user_founded)

    return user_founded


@router.get('/', response_model=UserPublicList, status_code=HTTPStatus.OK)
def read_users(
    session: SessionDB,  # type: ignore
):
    users = session.scalars(select(User)).all()

    return {'users': users}
