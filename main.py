from  aiogram import Bot , Dispatcher, executor, types
from dotenv import load_dotenv
from os import getenv

load_dotenv()
BOT_TOKEN ="5927903737:AAFGIJL8sWGNec_M2zoDXruwT65tmS5ziuE"
#наш бот
bot = Bot(BOT_TOKEN)
#диспетчер, получает сообщения, обрабатывает через обработчик
dp = Dispatcher(bot)



@dp.message_handler(commands=["start"])
async def start_command(message:types.Message):
   """
   Функция приветствия пользователя по имени
   """
   print(f"{message.from_user.id=}")
   print(f"{message.from_user.first_name=}")
   print(f"{message.from_user.last_name=}")
   print(f"{message.from_user.full_name=}")
   print(f"{message.from_user.username=}")
   print(f"{message.from_user.locale=}")


   await message.answer(text=f"Привет,{message.from_user.first_name},я бот BotNurisa")
   await message.delete()





@dp.message_handler(commands="picture")
async def image_sender(message:types.Message):
    """
    Функция ответа пользователю картинкой
    :param message:
    :return:
    """
    await message.answer_photo(
        open('./img.jpg','rb'),

    )
    await message.delete()


@dp.message_handler(commands=["help"])
async def help_command(message:types.Message):
   """
   Функция приветствия пользователя по имени
   """
   await message.answer(text=f"список команд с описанием {message.from_user.first_name}")
   await message.delete()

@dp.message_handler()
async def echo (message:types.Message):
   """
   Функция ответа пользователю заглавными буквами
   """
   await message.reply(text =message.text.upper())


if __name__ == "__main__":
    executor.start_polling(dp)