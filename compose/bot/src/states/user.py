from aiogram.dispatcher.filters.state import State, StatesGroup


class MainMenu(StatesGroup):
    MAIN_MENU = State()


class EncryptDecryptMenu(StatesGroup):
    SELECT_CIPHER = State()
    ENTER_CAESAR_SHIFT = State()
    ENTER_VERNAM_KEY = State()
    ENTER_VIGENERE_KEY = State()
    SELECT_MODE = State()
    SEND_MESSAGE_FOR_CIPHER = State()
