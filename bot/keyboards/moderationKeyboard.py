from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.callbacks.ModerationCallbackFactory import ModerationCallbackFactory, Action
from bot.labels.buttonLabels import MODERATION_CHANGE_TITLE_BUTTON, MODERATION_CHANGE_PERFORMER_BUTTON, \
    MODERATION_CHANGE_GENRE_BUTTON, MODERATION_ADD_AUDIO_FILE_BUTTON, MODERATION_ACCEPT_BUTTON, \
    MODERATION_DECLINE_BUTTON, MODERATION_CLOSE_BUTTON, CANCEL_BUTTON


def get_moderation_keyboard(audio_id: int):
    change_title = ModerationCallbackFactory(audio_id=audio_id, action=Action.change_title).pack()
    performer = ModerationCallbackFactory(audio_id=audio_id, action=Action.change_performer).pack()
    change_genre = ModerationCallbackFactory(audio_id=audio_id, action=Action.change_genre).pack()
    add_audio_file = ModerationCallbackFactory(audio_id=audio_id, action=Action.change_audio_file).pack()
    accept = ModerationCallbackFactory(audio_id=audio_id, action=Action.accept).pack()
    decline = ModerationCallbackFactory(audio_id=audio_id, action=Action.decline).pack()
    close = ModerationCallbackFactory(audio_id=audio_id, action=Action.close).pack()
    keyboard = [
        [InlineKeyboardButton(text=MODERATION_CHANGE_TITLE_BUTTON, callback_data=change_title)],
        [InlineKeyboardButton(text=MODERATION_CHANGE_PERFORMER_BUTTON, callback_data=performer)],
        [InlineKeyboardButton(text=MODERATION_CHANGE_GENRE_BUTTON, callback_data=change_genre)],
        [InlineKeyboardButton(text=MODERATION_ADD_AUDIO_FILE_BUTTON, callback_data=add_audio_file)],
        [InlineKeyboardButton(text=MODERATION_ACCEPT_BUTTON, callback_data=accept),
         InlineKeyboardButton(text=MODERATION_DECLINE_BUTTON, callback_data=decline)],
        [InlineKeyboardButton(text=MODERATION_CLOSE_BUTTON, callback_data=close)],
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup


def get_cancel_keyboard(audio_id):
    cancel = ModerationCallbackFactory(audio_id=audio_id, action=Action.cancel).pack()
    keyboard = [
        [InlineKeyboardButton(text=CANCEL_BUTTON, callback_data=cancel)]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup
