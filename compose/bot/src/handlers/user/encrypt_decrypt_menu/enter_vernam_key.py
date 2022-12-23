from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.user import EncryptDecryptMenu
from switchers import user
from views import buttons, messages


@dp.message_handler(text=buttons.back, state=EncryptDecryptMenu.ENTER_VERNAM_KEY)
async def back(message: types.Message):
    await user.select_cipher(message)


@dp.message_handler(state=EncryptDecryptMenu.ENTER_VERNAM_KEY)
async def enter_vernam_key(message: types.Message, state: FSMContext):
    try:
        key = [int(_) for _ in message.text.split(' ')]
    except ValueError:
        return await message.answer(messages.NOT_NUMERIC)

    for shift in key:
        if not 0 <= shift <= 25:
            return await message.answer(messages.INCORRECT_VERNAM_SHIFT)

    async with state.proxy() as data:
        data['vernam_key'] = key

    await user.send_message_for_cipher(message)
