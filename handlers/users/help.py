from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("1. /start tugmasini bo'sing\n",
            "2. Kanalga obuna bo'ling.\n",
            "3. Referal havolangizni do'stalrizga yubo'ring.\n",
            "4. Giveaway tugamaguncha bot va kanalni tark etmang.")
    
    await message.answer("\n".join(text))
