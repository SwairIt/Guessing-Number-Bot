from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database.orm_query import orm_add_points, orm_get_user_points

from keyboard.reply import start_kb


router = Router()


@router.message(StateFilter(None), Command("start"))
async def start(message: types.Message, session: AsyncSession):
    user_id = message.from_user.id

    user_points = await orm_get_user_points(session, user_id)

    if not user_points:
        await orm_add_points(session, {"user_id": user_id, "quantity": 0})
    await message.answer('Добро пожаловать в "Угадай число", выбери что хочешь сделать.', reply_markup=start_kb)


@router.callback_query(StateFilter(None), F.data == "to_main")
async def to_main(callback: types.CallbackQuery):
    await callback.answer("Ты перемещен на главную")
    await callback.message.answer('Добро пожаловать в "Угадай число", выбери что хочешь сделать.', reply_markup=start_kb)