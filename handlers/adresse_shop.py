from aiogram import types


async def adresse_shop(cb: types.CallbackQuery):
    """
        Ответ на нажатие кнопки адресса
    """
    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text='Мы находимя в Москве, ул. Нипольская ,дом 4',
    )