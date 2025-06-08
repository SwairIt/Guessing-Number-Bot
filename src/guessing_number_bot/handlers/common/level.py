from aiogram import F, Router, types
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext


import random

from handlers.common.game import GuessingNumber

from keyboard.reply import delete_kb


router = Router()


@router.callback_query(StateFilter(None), F.data == 'easy')
async def easy_level(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer("Ты выбрал легкий уровень")
    await callback.message.answer("Бот загадал число от 1 до 10, попробуй угадать!", reply_markup=delete_kb)
    GuessingNumber.number = random.randint(1, 11)
    GuessingNumber.level = 'easy'
    await state.set_state(GuessingNumber.guessing)


@router.callback_query(StateFilter(None), F.data == 'medium')
async def medium_level(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer("Ты выбрал средний уровень")
    await callback.message.answer("Бот загадал число от 1 до 100, попробуй угадать!", reply_markup=delete_kb)
    GuessingNumber.number = random.randint(1, 101)
    GuessingNumber.level = 'medium'
    await state.set_state(GuessingNumber.guessing)


@router.callback_query(StateFilter(None), F.data == 'hard')
async def hard_level(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer("Ты выбрал тяжелый уровень")
    await callback.message.answer("Бот загадал число от 1 до 1000, попробуй угадать!", reply_markup=delete_kb)
    GuessingNumber.number = random.randint(1, 1001)
    GuessingNumber.level = 'hard'
    await state.set_state(GuessingNumber.guessing)