from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from bot.labels.buttonLabels import CATALOG_BUTTON, PROFILE_BUTTON, SUPPORT_BUTTON


def get_menu_keyboard():
    keyboard = [
        [KeyboardButton(text=CATALOG_BUTTON)],
        [KeyboardButton(text=PROFILE_BUTTON), KeyboardButton(text=SUPPORT_BUTTON)],
    ]
    markup = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    return markup
