from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.database.Database import Database
from bot.keyboards.menuKeyboard import get_menu_keyboard
from bot.keyboards.profileKeyboard import get_profile_keyboard
from bot.labels.buttonLabels import PROFILE_BUTTON, SUPPORT_BUTTON, CATALOG_BUTTON
from bot.labels.messageLabels import START_MESSAGE, INDEV_MESSAGE, PROFILE_MESSAGE

router = Router()


@router.message(CommandStart())
async def start_command(message: Message, database: Database):
    await database.add_user(chat_id=message.from_user.id, username=message.from_user.username)
    await message.answer(START_MESSAGE, reply_markup=get_menu_keyboard())
    await message.delete()


@router.message(F.text == CATALOG_BUTTON)
async def catalog_button(message: Message):
    await message.answer(INDEV_MESSAGE)


@router.message(F.text == PROFILE_BUTTON)
async def profile_button(message: Message, database: Database):
    chat_id = message.from_user.id
    user = await database.get_user(chat_id=message.from_user.id)
    await message.answer(
        PROFILE_MESSAGE.format(
            id=user.id, username=user.username, registered_at=user.registered_at.strftime('%H:%M %d.%m.%Y')
        ),
        reply_markup=get_profile_keyboard(chat_id=chat_id)
    )
    await message.delete()


@router.message(F.text == SUPPORT_BUTTON)
async def support_button(message: Message):
    await message.answer(INDEV_MESSAGE)
