from sqlalchemy import BigInteger
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    ...


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, unique=True, 
                                     doc='ID пользователя')
    quantity: Mapped[int] = mapped_column(default=0, server_default='0', 
                                     doc='Количество очков пользователя')
    attempts: Mapped[int] = mapped_column(default=0, server_default='0', 
                                     doc='Количество попыток пользователя')
    games: Mapped[int] = mapped_column(default=0, server_default='0', 
                                     doc='Количество игр пользователя')
    winner_games: Mapped[int] = mapped_column(default=0, server_default='0', 
                                     doc='Количество выигранных игр пользователя')
    first_name: Mapped[str] = mapped_column(nullable=True)