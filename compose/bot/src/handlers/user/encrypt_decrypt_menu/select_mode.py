from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.user import EncryptDecryptMenu
from switchers import user
from views import buttons


@dp.message_handler(text=buttons.back, state=EncryptDecryptMenu.SELECT_MODE)
async def back(message: types.Message):
    await user.select_cipher(message)


@dp.message_handler(
    text=[buttons.encryption, buttons.decryption],
    state=EncryptDecryptMenu.SELECT_MODE,
)
async def select_mode(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['mode'] = message.text
        cipher = data['cipher']

    if cipher == buttons.caesar_cipher:
        return await user.enter_caesar_shift(message)

    if cipher == buttons.vigenere_cipher:
        return await user.enter_vigenere_key(message)

    if cipher == buttons.vernam_cipher and message.text == buttons.encryption:
        return await user.send_message_for_cipher(message)

    if cipher == buttons.vernam_cipher and message.text == buttons.decryption:
        return await user.enter_vernam_key(message)
