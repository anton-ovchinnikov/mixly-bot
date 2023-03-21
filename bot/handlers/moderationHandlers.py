from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.callbacks.ModerationCallbackFactory import ModerationCallbackFactory, Action
from bot.database.Database import Database
from bot.filters.IsAdmin import IsAdmin
from bot.keyboards.moderationKeyboard import get_cancel_keyboard, get_moderation_keyboard
from bot.labels.messageLabels import MODERATION_CHANGE_TITLE_MESSAGE, SUCCESS_CHANGE_TITLE_MESSAGE, \
    AUDIO_MODERATION_MESSAGE, MODERATION_CHANGE_PERFORMER_MESSAGE, SUCCESS_CHANGE_PERFORMER_MESSAGE
from bot.states.ModerationStates import ModerationStates

router = Router()


@router.callback_query(IsAdmin(), ModerationCallbackFactory.filter(F.action == Action.change_title))
async def change_title_button(query: CallbackQuery, state: FSMContext, callback_data: ModerationCallbackFactory):
    audio_id = callback_data.audio_id
    msg = await query.message.answer(MODERATION_CHANGE_TITLE_MESSAGE,
                                     reply_markup=get_cancel_keyboard(audio_id=audio_id))
    await state.set_state(ModerationStates.title)
    await state.set_data({
        'audio_id': audio_id,
        'messages_to_delete': [msg.message_id]
    })
    await query.message.delete()


@router.message(IsAdmin(), ModerationStates.title)
async def change_title(message: Message, database: Database, state: FSMContext, bot: Bot):
    chat_id = message.from_user.id
    sdata = await state.get_data()

    audio_id = sdata['audio_id']
    audio = await database.get_audio_by_id(audio_id=audio_id)
    audio.title = message.text
    await state.clear()
    await database.update_audio(audio)

    messages_to_delete = sdata['messages_to_delete']
    for msg in messages_to_delete:
        await bot.delete_message(chat_id=chat_id, message_id=msg)

    await message.answer(SUCCESS_CHANGE_TITLE_MESSAGE)
    if audio.file_id:
        msg = await bot.send_audio(chat_id=chat_id, audio=audio.file_id)
        await msg.edit_text(
            AUDIO_MODERATION_MESSAGE.format(title=audio.title, performer=audio.performer, genre=audio.genre),
            reply_markup=get_moderation_keyboard(audio_id=audio_id)
        )
    else:
        await message.answer(
            AUDIO_MODERATION_MESSAGE.format(title=audio.title, performer=audio.performer, genre=audio.genre),
            reply_markup=get_moderation_keyboard(audio_id=audio_id)
        )


@router.callback_query(IsAdmin(), ModerationCallbackFactory.filter(F.action == Action.change_performer))
async def change_performer_button(query: CallbackQuery, state: FSMContext, callback_data: ModerationCallbackFactory):
    audio_id = callback_data.audio_id
    msg = await query.message.answer(MODERATION_CHANGE_PERFORMER_MESSAGE,
                                     reply_markup=get_cancel_keyboard(audio_id=audio_id))
    await state.set_state(ModerationStates.performer)
    await state.set_data({
        'audio_id': audio_id,
        'messages_to_delete': [msg.message_id]
    })
    await query.message.delete()


@router.message(IsAdmin(), ModerationStates.performer)
async def change_performer(message: Message, database: Database, state: FSMContext, bot: Bot):
    chat_id = message.from_user.id
    sdata = await state.get_data()

    audio_id = sdata['audio_id']
    audio = await database.get_audio_by_id(audio_id=audio_id)
    audio.performer = message.text
    await state.clear()
    await database.update_audio(audio)

    messages_to_delete = sdata['messages_to_delete']
    for msg in messages_to_delete:
        await bot.delete_message(chat_id=chat_id, message_id=msg)

    await message.answer(SUCCESS_CHANGE_PERFORMER_MESSAGE)
    if audio.file_id:
        msg = await bot.send_audio(chat_id=chat_id, audio=audio.file_id)
        await msg.edit_text(
            AUDIO_MODERATION_MESSAGE.format(title=audio.title, performer=audio.performer, genre=audio.genre),
            reply_markup=get_moderation_keyboard(audio_id=audio_id)
        )
    else:
        await message.answer(
            AUDIO_MODERATION_MESSAGE.format(title=audio.title, performer=audio.performer, genre=audio.genre),
            reply_markup=get_moderation_keyboard(audio_id=audio_id)
        )


@router.callback_query(IsAdmin(), ModerationCallbackFactory.filter(F.action == Action.close))
async def close_button(query: CallbackQuery, callback_data: ModerationCallbackFactory, database: Database):
    audio_id = callback_data.audio_id
    audio = await database.get_audio_by_id(audio_id)
    audio.status = 'pending'
    await database.update_audio(audio)
    await query.message.delete()


@router.callback_query(IsAdmin(), ModerationCallbackFactory.filter(F.action == Action.cancel))
async def close_button(query: CallbackQuery, callback_data: ModerationCallbackFactory, database: Database,
                       state: FSMContext, bot: Bot):
    chat_id = query.from_user.id

    await state.clear()
    await query.message.delete()

    audio_id = callback_data.audio_id
    audio = await database.get_audio_by_id(audio_id=audio_id)

    if audio.file_id:
        msg = await bot.send_audio(chat_id=chat_id, audio=audio.file_id)
        await msg.edit_text(
            AUDIO_MODERATION_MESSAGE.format(title=audio.title, performer=audio.performer, genre=audio.genre),
            reply_markup=get_moderation_keyboard(audio_id=audio_id)
        )
    else:
        await query.message.answer(
            AUDIO_MODERATION_MESSAGE.format(title=audio.title, performer=audio.performer, genre=audio.genre),
            reply_markup=get_moderation_keyboard(audio_id=audio_id)
        )
