from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from data.text import textHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    await message.answer(textHelp)
