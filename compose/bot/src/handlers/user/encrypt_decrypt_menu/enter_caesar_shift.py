from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.user import EncryptDecryptMenu
from switchers import user
from views import buttons, messages


@dp.message_handler(text=buttons.back, state=EncryptDecryptMenu.ENTER_CAESAR_SHIFT)
async def back(message: types.Message):
    await user.select_cipher(message)


@dp.message_handler(state=EncryptDecryptMenu.ENTER_CAESAR_SHIFT)
async def enter_caesar_shift(message: types.Message, state: FSMContext):
    try:
        shift = int(message.text)
    except ValueError:
        return await message.answer(messages.NOT_NUMERIC)

    if not 0 <= shift <= 25:
        return await message.answer(messages.INCORRECT_CAESAR_SHIFT)

    async with state.proxy() as data:
        data['caesar_shift'] = shift

    await user.send_message_for_cipher(message)
