from enum import Enum

from aiogram.filters.callback_data import CallbackData


class Action(str, Enum):
    add_audio = 'add_audio'
    cancel = 'cancel'


class ProfileCallbackFactory(CallbackData, prefix="profile"):
    chat_id: int
    action: Action
