from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.user import EncryptDecryptMenu
from switchers import user
from views import buttons


@dp.message_handler(text=buttons.back, state=EncryptDecryptMenu.SELECT_CIPHER)
async def back(message: types.Message):
    await user.main_menu(message)


@dp.message_handler(
    text=[buttons.caesar_cipher, buttons.vigenere_cipher, buttons.vernam_cipher],
    state=EncryptDecryptMenu.SELECT_CIPHER,
)
async def select_cipher(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['cipher'] = message.text

    await user.select_mode(message)
