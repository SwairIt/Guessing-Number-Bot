from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter

from sqlalchemy.ext.asyncio import AsyncSession

from database.orm_query import orm_add_db, orm_get_user_db

from keyboard.reply import start_kb


router = Router()


@router.message(StateFilter(None), Command("start"))
async def start(message: types.Message, session: AsyncSession):
    user_id = message.from_user.id

    user_db = await orm_get_user_db(session, user_id)

    try:
        user_db.id
    except AttributeError:
        print('Была создана бд для еще одного юзера')
        await orm_add_db(session, {"user_id": user_id, "quantity": 0, "attempts": 0, "games": 0, "winner_games": 0, "first_name": message.from_user.username})
    await message.answer('Добро пожаловать в "Угадай число", выбери что хочешь сделать.', reply_markup=start_kb)


@router.callback_query(StateFilter(None), F.data == "to_main")
async def to_main(callback: types.CallbackQuery):
    await callback.answer("Ты перемещен на главную")
    await callback.message.answer('Добро пожаловать в "Угадай число", выбери что хочешь сделать.', reply_markup=start_kb)