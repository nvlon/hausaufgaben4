
import asyncio

from aiogram import executor
from aiogram.dispatcher.filters import Text


from geschaft.admin import start_command
from geschaft.form_exe import (Form, adress_get, age_check, cancel_handler,
                                day_check, get_age, name_get, process_done)
from geschaft.help import i_am_trying
from geschaft.bot_kick import ban_user, check_message
from geschaft.myinfo_command import send_info
from geschaft.pictures import friend_picture
from geschaft.scheduler import schedule_command, scheduler
from geschaft.shop import shop_start
from geschaft.adresse_shop import adresse_shop



async def startup(_):
    """
        запускаем дополнительные сторонние сервисы
    """
    init()
    create_table()
    asyncio.create_task(scheduler())

#Регистрирую команду старт
dp.register_message_handler(start_command, commands=['start'])
#Регистрирую команду, которая выведет все команды
dp.register_message_handler(i_am_trying, commands=['help'])
#Регистрирую команду для выведения информации про пользователя
dp.register_message_handler(send_info, commands=['myinfo'])
#Регистрирую команду для отправки случайного картинки
dp.register_message_handler(friend_picture, commands=['picture'])
#Регистрирую первый отклик на inline keyboard button и вывожу keyboard button с товарами
dp.register_callback_query_handler(shop_start, text='shop_start')
#Регистрирую второй отклик на inline keyboard button, про адресс магазина
dp.register_callback_query_handler(shop_adress, text='shop_adress')
#Регистрирую отклики на keyboard button с товарами
dp.register_message_handler(Gesundheitsprodukte, Text(equals='Продукты для здоровья'))
#Регистрирую отклик на кнопку купить, вывожу анкету для заполнения
dp.register_callback_query_handler(name_get, Text(startswith='buy_item '))
#Сохраняю ответы пользователя
dp.register_message_handler(adress_get, state=Form.name)
dp.register_message_handler(get_age, state=Form.adress)
dp.register_message_handler(age_check, state=Form.age)
dp.register_message_handler(day_check, state=Form.day)
#Заношу данные пользователя, в случае правильного заполнения анкеты, в БД
dp.register_message_handler(process_done, Text(equals='Да'), state=Form.done)
#Отменяю неправильно-заполненную анкету и не сохраняю её в БД
dp.register_message_handler(name_get, Text(equals='Нет'), state=Form.done)
dp.register_message_handler(cancel_handler, state='*', commands='cancel')
dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
#Регистрирую напоминалку
dp.register_message_handler(schedule_command, Text(startswith="Напомнить "))
#Регистрирую команду бана пользователя в групповом чате при помощи команды
dp.register_message_handler(ban_user, commands=['да'], commands_prefix='!')
#Проверяю сообщения в групповом чате, на наличии плохих слов
dp.register_message_handler(check_message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=startup)