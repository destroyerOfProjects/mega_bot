from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from views import buttons

main_menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu_kb.row(KeyboardButton(buttons.start_encryption_or_decryption))

cipher_menu = ReplyKeyboardMarkup(resize_keyboard=True)
cipher_menu.row(
    KeyboardButton(buttons.caesar_cipher),
    KeyboardButton(buttons.vigenere_cipher),
    KeyboardButton(buttons.vernam_cipher),
)
cipher_menu.add(KeyboardButton(buttons.back))

back_kb = ReplyKeyboardMarkup(resize_keyboard=True)
back_kb.add(KeyboardButton(buttons.back))

mode_kb = ReplyKeyboardMarkup(resize_keyboard=True)
mode_kb.row(
    KeyboardButton(buttons.encryption),
    KeyboardButton(buttons.decryption),
)
mode_kb.add(KeyboardButton(buttons.back))
