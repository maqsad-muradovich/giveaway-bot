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
    try:
        text = int(message.text.split(" ")[1])
        if text != '':
            db.add_follower(user_id=text, follower_id=member.user.id)
            await bot.send_message(chat_id=text, text=f"Sizning havolangiz orqali {member.user.first_name} kanalga obuna boldi")
    except: 
        pass
    
    await message.answer(f"Assalomu aleykum")
    
    if member.status in ['member', 'administrator', 'creator']:
        await message.answer(f"Mana sizning referal havolangiz:\n{BOT_LINK}?start={member.user.id}")

        try:
            db.add_user(id=member.user.id, name=member.user.full_name)
        except sqlite3.IntegrityError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)
    else:
        await message.answer(text=f"Givda Ishtrok etish uchun qanalga obuna bo'ling:\n{CHANEL_LINK}", reply_markup=check_subscription)
