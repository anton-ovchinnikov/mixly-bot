from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.labels.buttonLabels import PREV_BUTTON, NEXT_BUTTON


def get_catalog_keyboard():
    keyboard = [
        [InlineKeyboardButton(text=PREV_BUTTON, callback_data='huy'),
         InlineKeyboardButton(text=NEXT_BUTTON, callback_data='huy')]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup
