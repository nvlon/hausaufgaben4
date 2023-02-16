from aiogram import Bot,Dispatcher,executor,types
from aiogram.dispatcher.filtres import Text
from dotenv import loar_dotenv
from os import getenv
import logging
from handlers import start
from handlers import i_am_trying
from handlers import send_info
from pictures.import friend_picture
from handlers import shop_start
from handlers import adresse_shop
from handlers import get_products
from handlers import buy_item

from handlers import(
    Form,
    cancel_handler,
    name_get,
    adress_get,
    get_age,
    age_check,
    day_check,
    process_done
)


from handlers import(
    check_message,
    ban_user
)


loar_dotenv()
bot= Bot (getenv ('MY_TOKEN'))
dp= Dispatcher(bot)

dp.register_message_handler(start,commands=['start'])
dp.register_message_handler(i_am_trying,commands=['help'])
dp.register_message_handler(send_info,commands=['myinfo'])
dp.register_message_handler(friend_picture,commands=['picture'])
dp.register_callback_query_handler(shop_start, command=['shop_start'])
dp.register_callback_query_handler(adresse_shop, command=['adresse_shop'])
dp.register_message_handler(get_products,Text(equals='Продукты для здоровья') )
dp.register_callback_query_handler(name_get,Text(startwith='byi_item'))
dp.register_message_handler(name_get, commands=['form'])
dp.register_message_handler(name_get, Text(equals='Нет'),state=Form.done)
dp.register_message_handler(cancel_handler, state='*', commands='cancel')
dp.register_message_handler(cancel_handler, Text(equals='cancel,ignore_case=True'),state='*')
dp.register_message_handler(adress_get, state=Form.name)
dp.message_handler(get_age,state=Form.adress)
dp.register_message_handler(age_chek,state=Form.age )
dp.register_message_handler(age_chek,state=Form.day )
dp.register_message_handler(process_done, Text(equals='Да'),state=Form.done)
dp.register_message_handler(ban_user,commands=['да'],commands_prefix='!' )
dp.register_message_handler(check_message)





if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp,skip_updates=True, on_startup=startup)
