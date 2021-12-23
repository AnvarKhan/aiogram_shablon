from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⛰Turi"),
        ],
        [
            KeyboardButton(text="🏬Gosti"),
        ],
        [
            KeyboardButton(text="🧍🏻‍♂️Gidi"),
        ],
    ],
    resize_keyboard=True
)