from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboard.inline import choose_level_kb, easy_again_markup, medium_again_markup, hard_again_markup
from keyboard.reply import start_kb, delete_kb


router = Router()


class GuessingNumber(StatesGroup):
    level = ''
    attempts = 0
    number = 0
    guessing = State()


@router.message(StateFilter(None), F.text == "Играть")
async def play(message: types.Message):
    await message.answer('Выбери режим(подробнее о режимах можешь посмотреть в пункте "О боте")', reply_markup=choose_level_kb())


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
            if GuessingNumber.level == 'easy':
                await message.answer(f"Верно! Ты угадал с {GuessingNumber.attempts} попытки! Попробуй еще раз.", reply_markup=easy_again_markup())
            elif GuessingNumber.level == 'medium':
                await message.answer(f"Верно! Ты угадал с {GuessingNumber.attempts} попытки! Попробуй еще раз.", reply_markup=medium_again_markup())
            elif GuessingNumber.level == 'hard':
                await message.answer(f"Верно! Ты угадал с {GuessingNumber.attempts} попытки! Попробуй еще раз.", reply_markup=hard_again_markup())
            await state.clear()
            GuessingNumber.attempts = 0
    except ValueError:
        await message.answer("Введи число!")
        print("Человек ввел не число")


@router.message(GuessingNumber.guessing)
async def guessing_number_wrong(message: types.Message):
    await message.answer("Введи число!")