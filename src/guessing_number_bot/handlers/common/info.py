from aiogram import F, Router, types


router = Router()


@router.message(F.text == "Моя статистика")
async def statistics(message: types.Message):
    await message.answer('...')


@router.message(F.text == "О боте")
async def statistics(message: types.Message):
    await message.answer('<i>By @HiL1ne</i>\n\n<b>Режимы:</b>\n\nСуществует 3 режима игры\n\nЛегкий --> Бот загадывает число от 0 до 10, за победу ты получаешь 5 очков\n\nСредний --> Бот загадывает число от 0 до 100, за победу ты получаешь 15 очков\n\nТяжелый --> Бот загадывает число от 0 до 1000, за победу ты получаешь 50 очков\n\n<b>Удобные команды:</b>\n\nотмена или /отмена --> отменить игру\n\n')