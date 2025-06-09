from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import User


async def orm_add_db(session: AsyncSession, data: dict):
    obj = User(
        user_id=data["user_id"],
        quantity=data["quantity"],
        attempts=data["attempts"],
        games=data["games"],
        winner_games=data["winner_games"]
    )
    session.add(obj)
    await session.commit()


async def orm_update_db(session: AsyncSession, user_id: int, new_quantity: int, new_attempts: int, new_games: int, new_winner_games: int):
    query = update(User).where(User.user_id == user_id).values(quantity=new_quantity, attempts=new_attempts, games=new_games, winner_games=new_winner_games)
    await session.execute(query)
    await session.commit()


async def orm_get_user_db(session: AsyncSession, user_id: int):
    result = await session.execute(
        select(User).where(User.user_id == user_id)
    )
    return result.scalar_one_or_none()


async def increment_user_db(session: AsyncSession, user_id: int, value_points: int, value_attempts: int, value_games: int, value_winner_games: int):
    await session.execute(update(User).where(User.user_id == user_id).values(quantity=User.quantity + value_points, attempts=User.attempts + value_attempts, games=User.games + value_games, winner_games=User.winner_games + value_winner_games))
    await session.commit()


