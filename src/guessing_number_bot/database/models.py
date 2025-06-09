from sqlalchemy import BigInteger
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    ...


class Points(Base):
    __tablename__ = 'points'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, unique=True, 
                                     doc='ID пользователя')
    quantity: Mapped[int] = mapped_column(default=0, server_default='0', 
                                     doc='Количество очков пользователя')