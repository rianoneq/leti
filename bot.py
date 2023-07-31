import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import executor
from aiogram import types

from data.config import CONFIG_DATA

from scripts.main import General

from data.models import SNILS

API_TOKEN = CONFIG_DATA['API_TOKEN']

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
  """
  This handler will be called when user sends `/start` or `/help` command
  """
  await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler(commands=['balls'])
async def welcome(message: types.Message):
  """
  This handler will be called when user sends `/start` or `/help` command
  """
  await message.reply(General(166).main())


@dp.message_handler(commands=['snils'])
async def welcome(message: types.Message):
  """
  This handler will be called when user sends `/start` or `/help` command
  """

  await message.reply(General('160-461-141 26').main())

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)