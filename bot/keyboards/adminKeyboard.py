from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.callbacks.AdminCallbackFactory import AdminCallbackFactory, Action
from bot.labels.buttonLabels import ADMIN_MODERATION_BUTTON


def get_admin_keyboard(chat_id: int):
    moderation = AdminCallbackFactory(chat_id=chat_id, action=Action.moderation).pack()
    keyboard = [
        [InlineKeyboardButton(text=ADMIN_MODERATION_BUTTON, callback_data=moderation)]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup
