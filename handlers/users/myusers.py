from aiogram import types
from loader import dp, db

@dp.message_handler(commands='myusers')
async def my_users(message: types.Message):
    text = db.get_followers_list(user_id=message.from_user.id)
    await message.answer(f"Siz chaqirgan akkauntlar soni: {len(text)}")