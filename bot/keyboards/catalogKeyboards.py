from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.callbacks.CatalogPaginationCallbackFactory import CatalogPaginationCallbackFactory, Action
from bot.labels.buttonLabels import BACK_BUTTON, NEXT_BUTTON, CLOSE_BUTTON


def get_catalog_pagination_keyboard(offset: int = 0, is_max_offset: bool = False):
    next_cb = CatalogPaginationCallbackFactory(offset=offset + 10, action=Action.next).pack()
    back_cb = CatalogPaginationCallbackFactory(offset=offset - 10 if offset > 0 else 0, action=Action.back).pack()
    close = CatalogPaginationCallbackFactory(offset=0, action=Action.close).pack()

    next_keyboard = [
        [InlineKeyboardButton(text=NEXT_BUTTON, callback_data=next_cb)],
        [InlineKeyboardButton(text=CLOSE_BUTTON, callback_data=close)]
    ]
    back_keyboard = [
        [InlineKeyboardButton(text=BACK_BUTTON, callback_data=back_cb)],
        [InlineKeyboardButton(text=CLOSE_BUTTON, callback_data=close)]
    ]
    full_keyboard = [
        [InlineKeyboardButton(text=BACK_BUTTON, callback_data=back_cb),
         InlineKeyboardButton(text=NEXT_BUTTON, callback_data=next_cb)],
        [InlineKeyboardButton(text=CLOSE_BUTTON, callback_data=close)]

    ]
    markup = InlineKeyboardMarkup(inline_keyboard=full_keyboard)

    if offset == 0:
        markup = InlineKeyboardMarkup(inline_keyboard=next_keyboard)
    elif is_max_offset:
        markup = InlineKeyboardMarkup(inline_keyboard=back_keyboard)
    return markup
