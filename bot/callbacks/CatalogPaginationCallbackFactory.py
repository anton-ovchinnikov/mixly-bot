from enum import Enum

from aiogram.filters.callback_data import CallbackData


class Action(str, Enum):
    back = 'back'
    next = 'next'
    close = 'close'


class CatalogPaginationCallbackFactory(CallbackData, prefix="pagination"):
    offset: int
    action: Action
