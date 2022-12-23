from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from loader import bot, dp
from handlers import dp


async def on_shutdown(dispatcher: Dispatcher):
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()


if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=on_shutdown)
