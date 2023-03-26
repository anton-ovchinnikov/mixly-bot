from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.labels.buttonLabels import PREV_BUTTON, NEXT_BUTTON


def get_catalog_keyboard(page: int = 0):
    next_keyboard = [
        [InlineKeyboardButton(text=NEXT_BUTTON, callback_data='huy')]
    ]
    full_keyboard = [
        [InlineKeyboardButton(text=PREV_BUTTON, callback_data='huy'),
         InlineKeyboardButton(text=NEXT_BUTTON, callback_data='huy')]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=full_keyboard if page != 0 else next_keyboard)
    return markup
