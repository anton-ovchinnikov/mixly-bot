from enum import Enum

from aiogram.filters.callback_data import CallbackData


class Action(str, Enum):
    moderation = 'moderation'
    cancel = 'cancel'


class AdminCallbackFactory(CallbackData, prefix="admin"):
    chat_id: int
    action: Action
