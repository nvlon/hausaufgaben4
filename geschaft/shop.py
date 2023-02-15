from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

shop_kb = ReplyKeyboardMarkup(resize_keyboard=True)
shop_kb.add(
    KeyboardButton('Продукты для здоровья'),
    KeyboardButton('Уход за кожей'),

)
async def shop_start(cb:types.CallbackQuery):
    """
    Ответ на нажатие кнопки магазина.
    Показываем категории кнопками
    """
    await cb.bot.send_message(
        chat_id=cb.from_user.id,
        text='Что вас интересует?',
        reply_markup=shop_kb
    )