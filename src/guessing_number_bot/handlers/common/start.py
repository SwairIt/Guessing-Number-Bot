from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import random

from keyboard.inline import again_markup
from keyboard.reply import start_kb, delete_kb


router = Router()


@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer('Добро пожаловать в "Угадай число", выберите что хотите сделать.', reply_markup=start_kb)


@router.message(F.text == "Моя статистика")
async def statistics(message: types.Message):
    await message.answer('...')


@router.message(F.text == "О боте")
async def statistics(message: types.Message):
    await message.answer('<i>By @HiL1ne</i>\n\n<b>Режимы:</b>\n\nСуществует 3 режима игры\n\nЛегкий --> Бот загадывает число от 0 до 10, за победу ты получаешь 5 очков\n\nСредний --> Бот загадывает число от 0 до 100, за победу ты получаешь 15 очков\n\nТяжелый --> Бот загадывает число от 0 до 1000, за победу ты получаешь 50 очков\n\n<b>Удобные команды:</b>\n\nотмена или /отмена --> отменить игру\n\n')


################# FSM #################################################


class GuessingNumber(StatesGroup):
    attempts = 0
    number = random.randint(1, 101)
    guessing = State()


@router.message(StateFilter(None), F.text == "Играть")
async def play(message: types.Message, state: FSMContext):
    await message.answer("Бот загадал число от 1 до 100, попробуйте угадать!", reply_markup=delete_kb)
    await state.set_state(GuessingNumber.guessing)


@router.callback_query(StateFilter(None), F.data == "play_again")
async def again(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer("Играйте")
    await callback.message.answer("Бот загадал число от 1 до 100, попробуйте угадать!")
    await state.set_state(GuessingNumber.guessing)


@router.message(StateFilter('*'), Command("отмена"))
@router.message(StateFilter('*'), F.text.casefold() == "отмена")
async def cancel_handler(message: types.Message, state: FSMContext) -> None:

    current_state = await state.get_state()
    if current_state is None:
        return

    await state.clear()
    await message.answer("Вы не захотели играть? Ну и ладно!", reply_markup=start_kb)


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
        await message.answer("Введите число!")
        print("Человек ввел не число")



@router.message(GuessingNumber.guessing)
async def guessing_number_wrong(message: types.Message, state: FSMContext):
    await message.answer("Введите число!")