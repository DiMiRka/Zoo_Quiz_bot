import asyncio

import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram import F
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.utils.formatting import (
    Bold, as_list, as_marked_section
)

from token_data import TOKEN
from quiz_handler import router_1

dp = Dispatcher(storage=MemoryStorage())
dp.include_router(router_1)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[[types.KeyboardButton(text='Начать викторину!')]],
        resize_keyboard=True,
    )
    await message.answer(f'Привет! Этот бот выберет твоё тотемное животное на основе Викторины!',
                         reply_markup=keyboard)


@dp.message(F.animation)
async def id_send(message: Message):
    print(message.animation.file_id)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())