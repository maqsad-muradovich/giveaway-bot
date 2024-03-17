from aiogram import types
from loader import dp, db, bot
from data.config import CHANEL_ID

@dp.message_handler(commands='myusers')
async def my_users(message: types.Message):
    usersList = db.get_followers_list(user_id=message.from_user.id)
    countUsers = int()
    for userId in usersList:
        member = await bot.get_chat_member(chat_id=CHANEL_ID, user_id=userId)
        if member.status in ['member', 'administrator', 'creator']:
            countUsers += 1
    await message.answer(f"Siz chaqirgan akkauntlar soni: {countUsers}")