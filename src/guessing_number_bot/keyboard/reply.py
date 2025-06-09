from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Играть"), KeyboardButton(text="Моя статистика")],
        [KeyboardButton(text="О боте"), KeyboardButton(text="Рейтинговая таблица")]
    ],
    resize_keyboard=True, 
    input_field_placeholder="Выберите пункт меню"
)

delete_kb = ReplyKeyboardRemove()