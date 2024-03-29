from aiogram import types

from loader import dp, db, bot
from data.text import textReferalLink
from data.config import CHANEL_ID, BOT_LINK



@dp.callback_query_handler(lambda c: c.data == 'check_subscription')
async def process_callback_button(callback_query: types.CallbackQuery):
    
    member = await bot.get_chat_member(chat_id=CHANEL_ID, user_id=callback_query.from_user.id)
    
    if member.status in ['member', 'administrator']:
        referral_link = f"{BOT_LINK}?start={member.user.id}"
        await callback_query.answer(f"Rahmat")
        await bot.send_message(chat_id=member.user.id, text=f"{textReferalLink} {referral_link}")
        try:
            db.add_user(id=member.user.id, name=member.user.full_name)
        except:
            pass
    else:
        await callback_query.answer(f"Yana bir bor urunib ko'ring")