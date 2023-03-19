from aiogram.filters import Filter
from aiogram.types import CallbackQuery, Message

from bot.configreader import config


class IsAdmin(Filter):
    def __init__(self) -> None:
        pass

    async def __call__(self, event: [Message, CallbackQuery]) -> bool:
        admin_id = config.admin_id
        chat_id = event.from_user.id
        return True if chat_id == admin_id else False
