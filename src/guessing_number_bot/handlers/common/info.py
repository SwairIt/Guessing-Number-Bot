from aiogram import F, Router, types

from sqlalchemy.ext.asyncio import AsyncSession

from database.orm_query import orm_get_user_db, orm_get_all_dbs


router = Router()


@router.message(F.text == "Моя статистика")
async def statistics(message: types.Message, session: AsyncSession):
    user_db = await orm_get_user_db(session, message.from_user.id)
    points = user_db.quantity
    attempts = user_db.attempts
    games = user_db.games
    winner_games = user_db.winner_games
    cancelled_games = games - winner_games
    await message.answer(f'<i>By @HiL1ne</i>\n\n<b>Статистика игрока @{message.from_user.username}:</b>\n\nВсего очков --> {points}\n\nВсего попыток --> {attempts}\n\nВсего начатых игр --> {games}\n\nВсего выигранных игр --> {winner_games}\n\nВсего отмененных игр --> {cancelled_games}')


@router.message(F.text == "О боте")
async def statistics(message: types.Message):
    await message.answer('<i>By @HiL1ne</i>\n\n<b>Режимы:</b>\n\nСуществует 3 режима игры\n\nЛегкий --> Бот загадывает число от 0 до 10, за победу ты получаешь 5 очков\n\nСредний --> Бот загадывает число от 0 до 100, за победу ты получаешь 15 очков\n\nТяжелый --> Бот загадывает число от 0 до 1000, за победу ты получаешь 50 очков\n\n<b>Удобные команды:</b>\n\nотмена или /отмена --> отменить игру\n\n')


@router.message(F.text == "Рейтинговая таблица")
async def rating_table(message: types.Message, session: AsyncSession):
    users = await orm_get_all_dbs(session)

    sorted_user_data = sorted(users, key=lambda user: user.quantity, reverse=True)

    result_message = "<i>By @HiL1ne</i>\n\n🏆 <b>Рейтинговая таблица:</b>\n\n"

    for index, user in enumerate(sorted_user_data, start=1):
        username = user.first_name
        result_message += f"<b>Топ {index} → @{username}</b>\n     Очков: <code>{user.quantity}</code>\n\n"
    
    await message.answer(result_message)