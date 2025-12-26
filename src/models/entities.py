from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_as_dataclass, registry, mapped_column
from sqlalchemy import func, ForeignKey
from .schemas import Role

table_registry = registry()


@table_registry.mapped_as_dataclass
class User:
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, init=False)
    name: Mapped[str]
    password: Mapped[str]
    role: Mapped[Role]
    email: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now(), nullable=False
    )
    
@table_registry.mapped_as_dataclass
class Message:
    __tablename__ = 'messages'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, init=False)
    text: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    created_at: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now(), nullable=False
    )
