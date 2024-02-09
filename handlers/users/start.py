import sqlite3

from aiogram import types
from aiogram.types import ChatMemberUpdated
from aiogram.dispatcher.filters.builtin import CommandStart

from data.text import txt
from loader import dp, db, bot
from keyboards.inline.InlineButtons import check_subscription
from data.config import CHANEL_ID, ADMINS, CHANEL_LINK, BOT_LINK

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):

    # Userning malumotlari
    member = await bot.get_chat_member(chat_id=CHANEL_ID, user_id=message.from_user.id)
    follower_id = str(message.text.split(" ")[7:])

    try:
        if member.status in ['member', 'administrator', 'creator']:
            try:
                db.add_user(id=member.user.id, name=member.user.full_name)
            except sqlite3.IntegrityError as er:
                await bot.send_message(chat_id=ADMINS[0], text=er)
        elif member.status in ['kicked', 'restricted', 'Bot']: #Agar user blockda bo'lsa
                await message.answer("Administrator bilan bog'laning")
        else:
            await message.answer(f"Botdan foydalanish uchun kanalga obuna bo'ling: {CHANEL_LINK}", reply_markup=check_subscription)
    except Exception as err:
        await bot.send_message(chat_id=ADMINS[0], text=f"{err}")
        await message.answer("Uzur tizimda nosozlik yuz berdi siz bilan tez orada adminlar bo'glanadi")



    # if follower_id != '':
    #     if follower_id != str(member.user.id):
    #         db.add_follower(user_id=follower_id, follower_id=member.user.id)
    #         await bot.send_message(chat_id=follower_id, text=f"count followers")
    #     else:
    #         await message.answer("O'zizni havolangizdan registratsiyadan o'tish mumkin emas!")