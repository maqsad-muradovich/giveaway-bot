from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

check_subscription = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="check subscription", callback_data="check_subscription")]
])