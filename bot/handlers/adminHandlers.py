from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from bot.callbacks.AdminCallbackFactory import AdminCallbackFactory, Action
from bot.filters.IsAdmin import IsAdmin
from bot.keyboards.adminKeyboard import get_admin_keyboard
from bot.labels.messageLabels import ADMIN_MENU_MESSAGE

router = Router()


@router.message(IsAdmin(), Command('admin'))
async def admin_command(message: Message):
    await message.answer(
        ADMIN_MENU_MESSAGE, reply_markup=get_admin_keyboard(chat_id=message.from_user.id)
    )
    await message.delete()


@router.callback_query(IsAdmin(), AdminCallbackFactory.filter(F.action == Action.moderation))
async def moderation_button(query: CallbackQuery):
    await query.answer()
