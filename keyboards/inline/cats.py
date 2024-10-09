from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

cats = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Yavvoyi mushuklar", callback_data='yavvoyi'), InlineKeyboardButton(text="Uy mushuklari", callback_data="uy")]
    ]
)