from time import time

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN


#Инициализация
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    print(user_name)
    await message.reply(f'Привет, {user_name}! Твой user id = {user_id}!')


@dp.message_handler(content_types=['text'])
async def echo(message: types.Message):
    await message.reply(message.text)


@dp.message_handler(content_types=['photo'])
async def photo_den(message: types.Message):
    chat_id = message.chat.id
    await bot.send_photo(chat_id, 'https://sobaky.info/wp-content/uploads/2018/02/1-4.jpg')

@dp.message_handler(content_types=['location'])
async def location(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, 'https://search-maps.yandex.ru/v1/?text=бесплатная+парковка&type=geo&lang=ru_RU&apikey=be119a13-f4a0-4d15-9426-a9cd62a1a4a5')


#Команда запуска бота
if __name__ == '__main__': #Всегда True
    executor.start_polling(dp)