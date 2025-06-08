from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

again_markup = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Сыграть еще раз ▶", callback_data="play_again"), 
     InlineKeyboardButton(text="На главную", callback_data="to_main")]
    ])