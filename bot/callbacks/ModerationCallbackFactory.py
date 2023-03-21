from enum import Enum

from aiogram.filters.callback_data import CallbackData


class Action(str, Enum):
    change_title = 'change_title'
    change_performer = 'change_performer'
    change_genre = 'change_genre'
    add_audio_file = 'add_audio_file'
    accept = 'accept'
    decline = 'decline'
    close = 'close'
    cancel = 'cancel'


class ModerationCallbackFactory(CallbackData, prefix="moderation"):
    audio_id: int
    action: Action
