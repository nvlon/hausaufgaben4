from aiogram import types
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.dispatcher import FSMContext




class UserForm(StatesGroup):
    name= State()
    age= State()


async def start_user_dialog(message: types.Message):
    await UserForm.name.set()
    await message.answer('Скажите ваше имя')


async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy()as data:
        #сохраняем данные о имени
        data['name']= message.text
    await UserForm.next()
    await message.answer('Укажите ваш возвраст')


async def process_age(message: types.Message,state:FSMContext):
    age= message.text
    if not age.is_nummeric():
        await message.reply('Вводите только цифры!')
    else:
        async with state.proxy() as data:
        #данные о возврасте
        data['age']=age
        print(data)

        await state.finish()
        await message.answer('Благодарим ,что пользуетесь нашим сервисом!')