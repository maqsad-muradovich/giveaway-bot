from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot
from data.text import txt

channel_id = -1002052112624
referral_links = {}

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    referral_param = message.get_args()

    if referral_param:
        referral_links[user_id] = int(referral_param)

    referrer_id = referral_links.get(user_id)


    # await message.answer(f"{txt['start'][message.from_user.language_code]}, {message.from_user.full_name}!\n{member}")
    try:
        member = await bot.get_chat_member(chat_id=channel_id, user_id=message.from_user.id)
        if member.status in ['member', 'administrator', 'creator']:
            await message.answer("Вы подписаны на канал.")
            channel_username = 'nimadurChanel'  # Замените на имя вашего канала
            referral_link = f"https://t.me/{channel_username}?start={user_id}"

            # Отправьте пользователю реферальную ссылку
            await message.answer(f"Ваша реферальная ссылка: {referral_link}")
        else:
            await message.answer("Подпишитесь на канал, чтобы использовать бота.")
    except Exception as e:
        await message.answer(f"Ошибка при проверке подписки: {e}")

