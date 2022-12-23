from aiogram import types

from loader import dp
from states.user import MainMenu
from switchers import user
from views import buttons


@dp.message_handler(text=buttons.start_encryption_or_decryption, state=MainMenu.MAIN_MENU)
async def start_encryption_or_decryption(message: types.Message):
    await user.select_cipher(message)

# @dp.message_handler(state=MainMenu.MAIN_MENU)
# async def burger_king_is_shit(message: types.Message):
#     await message.answer('Burger King is shit!!!!')
