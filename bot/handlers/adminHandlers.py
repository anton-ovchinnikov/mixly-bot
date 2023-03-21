from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from bot.callbacks.AdminCallbackFactory import AdminCallbackFactory, Action
from bot.database.Database import Database
from bot.filters.IsAdmin import IsAdmin
from bot.keyboards.adminKeyboard import get_admin_keyboard
from bot.keyboards.moderationKeyboard import get_moderation_keyboard
from bot.labels.messageLabels import ADMIN_MENU_MESSAGE, NO_AUDIO_FOR_MODERATION_NOTIFY, AUDIO_MODERATION_MESSAGE

router = Router()


@router.message(IsAdmin(), Command('admin'))
async def admin_command(message: Message):
    await message.answer(
        ADMIN_MENU_MESSAGE, reply_markup=get_admin_keyboard(chat_id=message.from_user.id)
    )
    await message.delete()


@router.callback_query(IsAdmin(), AdminCallbackFactory.filter(F.action == Action.moderation))
async def moderation_button(query: CallbackQuery, bot: Bot, database: Database):
    chat_id = query.from_user.id

    audio = await database.get_audio_for_moderation()
    if audio:
        audio.status = 'moderation'
        audio.moderated_by = chat_id
        await database.update_audio(audio)
        if audio.file_id:
            await bot.send_audio(
                chat_id=chat_id, audio=audio.file_id,
                caption=AUDIO_MODERATION_MESSAGE.format(title=audio.title, performer=audio.performer,
                                                        genre=audio.genre),
                reply_markup=get_moderation_keyboard(audio_id=audio.id)
            )
        else:
            await query.message.answer(
                AUDIO_MODERATION_MESSAGE.format(title=audio.title, performer=audio.performer, genre=audio.genre),
                reply_markup=get_moderation_keyboard(audio_id=audio.id)
            )
        await query.answer()
    else:
        await query.answer(NO_AUDIO_FOR_MODERATION_NOTIFY)
