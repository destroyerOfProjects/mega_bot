from aiogram import types

from loader import dp
from switchers import user


@dp.message_handler(commands=['start'], state='*')
async def start(message: types.Message):
    await user.main_menu(message)
