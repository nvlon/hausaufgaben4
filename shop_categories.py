from aiogram import types
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

byu_item_kb= InlineKeyboardMarkup()
byu_item_kb.add(
    InlineKeyboardButton('Купить ', callback_data='byu_item')
)
async def show_books(message:types.Message):
     """
     Показываем пользователю список книг
     :param message:
     :return:
     """
     await message.answer (text= "Вот наши книги:")
     await message.answer(text="Книга 1", reply_markup=byu_item_kb)
     await message.answer(text="Книга 2",reply_markup=byu_item_kb)
     await message.answer(text="Книга 3",reply_markup=byu_item_kb)

