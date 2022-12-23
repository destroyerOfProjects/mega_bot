from aiogram.dispatcher import FSMContext

from loader import dp
from states.user import EncryptDecryptMenu
from switchers import user
from views import buttons
from aiogram import types
from utils.ciphers import vigenere
from utils.ciphers import caesar, vernam
from typing import Optional, Union


@dp.message_handler(text=buttons.back, state=EncryptDecryptMenu.SEND_MESSAGE_FOR_CIPHER)
async def back(message: types.Message):
    await user.select_mode(message)


@dp.message_handler(state=EncryptDecryptMenu.SEND_MESSAGE_FOR_CIPHER)
async def send_message_for_cipher(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        result = regulator(
            cipher_type=data['cipher'],
            mode=data['mode'],
            shift=data.get('caesar_shift'),
            text=message.text,
            vigenere_key=data.get('vigenere_key'),
            vernam_key=data.get('vernam_key'),
        )

    # Отработал шифр Цезаря, или шифр Виженера, или шифр Вернама в режиме дешифровки
    if isinstance(result, str):
        await message.answer(result)

    # Отработал шифр Вернама
    elif isinstance(result, tuple):
        await message.answer(result[0])
        await message.answer(f'Ключ: {result[1]}')

    await user.main_menu(message)


def regulator(
        cipher_type: str,
        mode: str,
        shift: Optional[int],
        text: str,
        vigenere_key: Optional[str],
        vernam_key: Optional[list[int]],
) -> Union[str, tuple[str, list[int]]]:
    # Шифр цезаря, шифрование
    if cipher_type == buttons.caesar_cipher and mode == buttons.encryption:
        return caesar.encryption(text=text, shift=shift)

    # Шифр цезаря, дешифрование
    if cipher_type == buttons.caesar_cipher and mode == buttons.decryption:
        return caesar.decryption(text=text, shift=shift)

    # Шифр Виженера, шифрование
    if cipher_type == buttons.vigenere_cipher and mode == buttons.encryption:
        return vigenere.encryption(message=text, key=vigenere_key)

    # Шифр Виженера, дешифрование
    if cipher_type == buttons.vigenere_cipher and mode == buttons.decryption:
        return vigenere.decryption(message=text, key=vigenere_key)

    # Шифр Вернама, шифрование
    if cipher_type == buttons.vernam_cipher and mode == buttons.encryption:
        return vernam.encryption(message=text)

    # Шифр Вернама, дешифрование
    if cipher_type == buttons.vernam_cipher and mode == buttons.decryption:
        return vernam.decryption(message=text, key=vernam_key)
