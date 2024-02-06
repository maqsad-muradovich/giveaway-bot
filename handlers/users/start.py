from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot
from data.text import txt

channel_id = -1002052112624

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    
    # Userning idsi
    user_id = message.from_user.id

    # await message.answer(f"{user_id}")
    try:
        member = await bot.get_chat_member(chat_id=channel_id, user_id=message.from_user.id)
        if member.status in ['member', 'administrator', 'creator']:
            await message.answer("Вы подписаны на канал.")
            channel_username = 'nimadurChanel' 
            referral_link = f"https://t.me/{channel_username}?start={user_id}"

            # Отправьте пользователю реферальную ссылку
            await message.answer(f"Ваша реферальная ссылка: {referral_link}")
        else:
            await message.answer("Подпишитесь на канал, чтобы использовать бота.")
    except Exception as e:
        await message.answer(f"Ошибка при проверке подписки: {e}")

