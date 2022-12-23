from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.user import EncryptDecryptMenu
from switchers import user
from views import buttons


@dp.message_handler(text=buttons.back, state=EncryptDecryptMenu.ENTER_VIGENERE_KEY)
async def back(message: types.Message):
    await user.select_cipher(message)


@dp.message_handler(state=EncryptDecryptMenu.ENTER_VIGENERE_KEY)
async def enter_vigenere_key(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['vigenere_key'] = message.text

    await user.send_message_for_cipher(message)
