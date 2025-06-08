from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter

from keyboard.reply import start_kb


router = Router()


@router.message(StateFilter(None), Command("start"))
async def start(message: types.Message):
    await message.answer('Добро пожаловать в "Угадай число", выбери что хочешь сделать.', reply_markup=start_kb)


@router.callback_query(StateFilter(None), F.data == "to_main")
async def to_main(callback: types.CallbackQuery):
    await callback.answer("Ты перемещен на главную")
    await callback.message.answer('Добро пожаловать в "Угадай число", выбери что хочешь сделать.', reply_markup=start_kb)