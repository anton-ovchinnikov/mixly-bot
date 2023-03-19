from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.callbacks.ProfileCallbackFactory import ProfileCallbackFactory, Action
from bot.labels.buttonLabels import ADD_AUDIO_BUTTON, CANCEL_BUTTON


def get_profile_keyboard(chat_id: int):
    add_audio = ProfileCallbackFactory(chat_id=chat_id, action=Action.add_audio).pack()
    keyboard = [
        [InlineKeyboardButton(text=ADD_AUDIO_BUTTON, callback_data=add_audio)],
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup


def get_cancel_keyboard(chat_id: int):
    cancel = ProfileCallbackFactory(chat_id=chat_id, action=Action.cancel).pack()
    keyboard = [
        [InlineKeyboardButton(text=CANCEL_BUTTON, callback_data=cancel)],
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup
