import os
import logging #

from random import choice
from aiogram import Bot, Dispatcher, types, executor
from decouple import config

logging.basicConfig(level=logging.INFO)

API_TOKEN = config('API_TOKEN')
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

IMG_PATH = 'C:\Users\Dell\Downloads\Python\TelegramBot2\imag'

categories = ['фото','фотография','картинки']

answers = { 
    'cat': ['кот','кошка','котяра','котя'],
    'people': ['люди','общество','компания'],
    'space': ['космос','галактика'],
    'nature':['природа','деревья','лес']
}

def get_photo_by_category(category):
    path = f'{IMG_PATH}/{category}'
    files = os.listdir(path)
    imag = choice(files)
    return open(f'{path/imag}', 'rb')






@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Здравствуй, я Элоер👋")
    print(message)

dp.message_handler()
async def basic_answers(message: types.Message):
    triger1 = False
    category = ''

    words = message.text.split()
    for word in words:
        if word.lower() in categories:
            triger1 = True
            continue
        for key, value in answers.items():
            if word.lower() in value:
                vategory = key
         
    if triger1 and category:
        await message.answer_photo(get_photo_by_category(category))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)