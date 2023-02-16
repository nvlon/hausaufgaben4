from aiogram import Bot , types
from random import choice
from os import listdir

async def image_sender(message:types.Message):
    """
    Функция ответа пользователю картинкой
    :param message:
    :return:
    """
    await message.answer_photo(
        open('../images/img.jpg', 'rb'),

    )
    await message.delete()