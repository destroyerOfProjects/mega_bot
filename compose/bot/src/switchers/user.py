from aiogram import types

from states.user import EncryptDecryptMenu, MainMenu
from views import keyboards, messages


async def main_menu(message: types.Message):
    await MainMenu.MAIN_MENU.set()
    await message.answer(text=messages.MAIN_MENU, reply_markup=keyboards.main_menu_kb)


async def select_cipher(message: types.Message):
    await EncryptDecryptMenu.SELECT_CIPHER.set()
    await message.answer(text=messages.SELECT_CIPHER, reply_markup=keyboards.cipher_menu)


async def enter_caesar_shift(message: types.Message):
    await EncryptDecryptMenu.ENTER_CAESAR_SHIFT.set()
    await message.answer(messages.ENTER_CAESAR_SHIFT, reply_markup=keyboards.back_kb)


async def enter_vigenere_key(message: types.Message):
    await EncryptDecryptMenu.ENTER_VIGENERE_KEY.set()
    await message.answer(messages.ENTER_VIGENERE_KEY, reply_markup=keyboards.back_kb)


async def enter_vernam_key(message: types.Message):
    await EncryptDecryptMenu.ENTER_VERNAM_KEY.set()
    await message.answer(messages.ENTER_VERNAM_KEY, reply_markup=keyboards.back_kb)


async def select_mode(message: types.Message):
    await EncryptDecryptMenu.SELECT_MODE.set()
    await message.answer(messages.SELECT_MODE, reply_markup=keyboards.mode_kb)


async def send_message_for_cipher(message: types.Message):
    await EncryptDecryptMenu.SEND_MESSAGE_FOR_CIPHER.set()
    await message.answer(messages.SEND_MESSAGE_TO_CIPHER, reply_markup=keyboards.back_kb)
