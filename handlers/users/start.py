from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from .model import *


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("Assalamualaykum, \nKontaktingizni yuboring masalan (+998912345678)", reply_markup=menu)
