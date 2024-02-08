import sqlite3

from aiogram import types
from aiogram.types import ChatMemberUpdated
from aiogram.dispatcher.filters.builtin import CommandStart

from data.text import txt
from loader import dp, db, bot
from data.config import CHANEL, ADMINS

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    # Userning malumotlari
    user_id   = message.from_user.id
    user_name = message.from_user.full_name

    channel_link = 'https://t.me/isqilibBot'

    try:
        db.add_user(id=user_id, name=user_name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    member = await bot.get_chat_member(chat_id=CHANEL, user_id=message.from_user.id)
    try:
        if member.status in ['member', 'administrator', 'creator']:
            referral_link = f"{channel_link}?start={user_id}"
            await message.answer(f"Sizning referal havolangiz: {referral_link}")
        else:
            await message.answer(f"Botdan foydalanish uchun kanalga obuna bo'ling: {channel_link}")
    except Exception as e:
        await message.answer(txt["error"]["uz"])

    await message.answer(f"{message.text}")