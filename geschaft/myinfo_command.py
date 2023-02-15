from aiogram import types
from geschaft.constanst import INFO_TEXT

async def send_info(message: types.Message):
    """
    Функция предоставляет информацию о пользователе
    :param message:
    :return:
    """
    await message.answer(text=INFO_TEXT.format(
        id= message.from_user.id,
        first_name = message.from_user.first_name,
        username = message.from_user.username
    ))
    await message.delete()