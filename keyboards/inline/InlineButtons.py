from data.config import CHANEL_LINK

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

check_subscription = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kanalga obuna bo'lish", url=CHANEL_LINK),
            InlineKeyboardButton(text="Obunani tekshirish", callback_data="check_subscription")
        ]
    ]
)