from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import random

from keyboard.inline import again_markup
from keyboard.reply import start_kb, delete_kb


router = Router()


class GuessingNumber(StatesGroup):
    attempts = 0
    number = random.randint(1, 101)
    guessing = State()


@router.message(StateFilter(None), F.text == "Играть")
async def play(message: types.Message, state: FSMContext):
    await message.answer("Бот загадал число от 1 до 100, попробуй угадать!", reply_markup=delete_kb)
    await state.set_state(GuessingNumber.guessing)


@router.callback_query(StateFilter(None), F.data == "play_again")
async def again(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer("Можешь играть")
    await callback.message.answer("Бот загадал число от 1 до 100, попробуй угадать!")
    await state.set_state(GuessingNumber.guessing)


@router.message(StateFilter('*'), Command("отмена"))
@router.message(StateFilter('*'), F.text.casefold() == "отмена")
async def cancel_handler(message: types.Message, state: FSMContext) -> None:

    current_state = await state.get_state()
    if current_state is None:
        return

    await state.clear()
    await message.answer("Ты отменил игру!", reply_markup=start_kb)


@router.message(GuessingNumber.guessing, F.text)
async def guessing_number(message: types.Message, state: FSMContext):
    try:
        user_message = int(message.text)
        GuessingNumber.attempts += 1
        await state.update_data(guessing=user_message)
        if user_message > GuessingNumber.number:
            await message.answer("Неверно, число меньше")
            await state.set_state(GuessingNumber.guessing)
        elif user_message < GuessingNumber.number:
            await message.answer("Неверно, число больше")
            await state.set_state(GuessingNumber.guessing)
        else:
            await message.answer(f"Верно! Ты угадал с {GuessingNumber.attempts} попытки! Попробуй еще раз.", reply_markup=again_markup)
            await state.clear()
            GuessingNumber.attempts = 0
    except ValueError:
        await message.answer("Введи число!")
        print("Человек ввел не число")


@router.message(GuessingNumber.guessing)
async def guessing_number_wrong(message: types.Message):
    await message.answer("Введи число!")