from aiogram import types
from loader import dp
from views import messages


@dp.message_handler(commands=['help'], state='*')
async def help_command(message: types.Message):
    await message.answer(messages.HELP)
