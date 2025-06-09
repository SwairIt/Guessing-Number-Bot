from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Points


async def orm_add_points(session: AsyncSession, data: dict):
    obj = Points(
        user_id=data["user_id"],
        quantity=data["quantity"]
    )
    session.add(obj)
    await session.commit()


async def orm_update_points(session: AsyncSession, user_id: int, new_quantity: int):
    query = update(Points).where(Points.user_id == user_id).values(quantity=new_quantity)
    await session.execute(query)
    await session.commit()


async def orm_get_user_points(session: AsyncSession, user_id: int):
    result = await session.execute(
        select(Points).where(Points.user_id == user_id)
    )
    return result.scalar_one_or_none()


async def increment_points(session: AsyncSession, user_id: int, value: int):
    await session.execute(update(Points).where(Points.user_id == user_id).values(quantity=Points.quantity + value))
    await session.commit()