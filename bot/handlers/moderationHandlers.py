from aiogram import Router, F
from aiogram.types import CallbackQuery

from bot.callbacks.ModerationCallbackFactory import ModerationCallbackFactory, Action
from bot.database.Database import Database
from bot.filters.IsAdmin import IsAdmin

router = Router()


@router.callback_query(IsAdmin(), ModerationCallbackFactory.filter(F.action == Action.close))
async def close_button(query: CallbackQuery, callback_data: ModerationCallbackFactory, database: Database):
    audio_id = callback_data.audio_id
    audio = await database.get_audio_by_id(audio_id)
    audio.status = 'pending'
    await database.update_audio(audio)
    await query.message.delete()
