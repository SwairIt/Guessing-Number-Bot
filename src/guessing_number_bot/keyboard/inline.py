from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def choose_level_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="легкий", callback_data='easy'), 
         InlineKeyboardButton(text="средний", callback_data='medium'),
         InlineKeyboardButton(text="тяжелый", callback_data='hard')],
         [InlineKeyboardButton(text="назад", callback_data='to_main')]
    ])


def easy_again_markup() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Сыграть еще раз ▶", callback_data="easy"), 
        InlineKeyboardButton(text="На главную", callback_data="to_main")]
    ])


def medium_again_markup() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Сыграть еще раз ▶", callback_data="medium"), 
        InlineKeyboardButton(text="На главную", callback_data="to_main")]
    ])


def hard_again_markup() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Сыграть еще раз ▶", callback_data="hard"), 
        InlineKeyboardButton(text="На главную", callback_data="to_main")]
    ])