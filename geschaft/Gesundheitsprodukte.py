from aiogram import types
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from geschaft import get_products

def etwas_kaufen(product_id):
    etwas_kaufen=InlineKeyboardMarkup()
    etwas_kaufen.add(InlineKeyboardButton('Купить', callback_data=f'etwas_kaufen{product_id}'))
    return etwas_kaufen

async def Produkt_zeigen(message: types.Message):
    """
    Функция покажет витамины

    """
await message.answer(text='Вот продукты для здоровья:')
vitamine = get_products()[0]
superfood = get_products()[1]
krautertee = get_products()[2]
await message.answer_photo(
    open(vitamine[3], 'rb'),
    caption=f'{vitamine[1]}, стоимость - {vitamine[2]}',
    reply_markup=etwas_kaufen(vitamine[0])
)
await message.answer_photo(
    open(superfood[3], 'rb'),
    caption=f'{superfood[1]}, стоимость - {superfood[2]}',
    reply_markup=etwas_kaufen(superfood[0])
)
await message.answer_photo(
    open(krautertee[3], 'rb'),
    caption=f'{krautertee[1]}, стоимость - {krautertee[2]}',
    reply_markup=etwas_kaufen(krautertee[0])
)
