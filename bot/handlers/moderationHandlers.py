import os.path

from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.callbacks.ModerationCallbackFactory import ModerationCallbackFactory, Action
from bot.database.Database import Database
from bot.filters.IsAdmin import IsAdmin
from bot.keyboards.moderationKeyboard import get_cancel_keyboard, get_moderation_keyboard
from bot.labels.messageLabels import MODERATION_CHANGE_TITLE_MESSAGE, SUCCESS_CHANGE_TITLE_MESSAGE, \
    AUDIO_MODERATION_MESSAGE, MODERATION_CHANGE_PERFORMER_MESSAGE, SUCCESS_CHANGE_PERFORMER_MESSAGE, \
    MODERATION_CHANGE_AUDIO_FILE_MESSAGE, SUCCESS_CHANGE_AUDIO_FILE_MESSAGE, MODERATION_DECLINE_MESSAGE, \
    SUCCESS_DECLINE_MESSAGE, DECLINE_USER_MESSAGE, ACCEPT_USER_MESSAGE, SUCCESS_ACCEPT_MESSAGE
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
        await bot.send_audio(
            chat_id=chat_id, audio=audio.file_id,
            caption=AUDIO_MODERATION_MESSAGE.format(title=audio.title, performer=audio.performer, genre=audio.genre),
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
        await bot.send_audio(
            chat_id=chat_id, audio=audio.file_id,
            caption=AUDIO_MODERATION_MESSAGE.format(title=audio.title, performer=audio.performer, genre=audio.genre),
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
        await bot.send_audio(
            chat_id=chat_id, audio=audio.file_id,
            caption=AUDIO_MODERATION_MESSAGE.format(title=audio.title, performer=audio.performer, genre=audio.genre),
            reply_markup=get_moderation_keyboard(audio_id=audio_id)
        )
    else:
        await query.message.answer(
            AUDIO_MODERATION_MESSAGE.format(title=audio.title, performer=audio.performer, genre=audio.genre),
            reply_markup=get_moderation_keyboard(audio_id=audio_id)
        )


@router.callback_query(IsAdmin(), ModerationCallbackFactory.filter(F.action == Action.change_audio_file))
async def change_audio_file_button(query: CallbackQuery, state: FSMContext, callback_data: ModerationCallbackFactory):
    audio_id = callback_data.audio_id
    msg = await query.message.answer(MODERATION_CHANGE_AUDIO_FILE_MESSAGE,
                                     reply_markup=get_cancel_keyboard(audio_id=audio_id))
    await state.set_state(ModerationStates.audio_file)
    await state.set_data({
        'audio_id': audio_id,
        'messages_to_delete': [msg.message_id]
    })
    await query.message.delete()


@router.message(IsAdmin(), ModerationStates.audio_file, F.audio)
async def change_audio_file(message: Message, database: Database, state: FSMContext, bot: Bot):
    chat_id = message.from_user.id
    sdata = await state.get_data()

    file_id = message.audio.file_id
    file = await bot.get_file(file_id=file_id)
    file_path = file.file_path
    local_path = f'music/{file_id}.mp3'
    await bot.download_file(file_path=file_path, destination=local_path)

    audio_id = sdata['audio_id']
    audio = await database.get_audio_by_id(audio_id=audio_id)
    audio.file_id = file_id
    audio.local_path = local_path
    await database.update_audio(audio)

    await state.clear()
    messages_to_delete = sdata['messages_to_delete']
    for msg in messages_to_delete:
        await bot.delete_message(chat_id=chat_id, message_id=msg)

    await message.answer(SUCCESS_CHANGE_AUDIO_FILE_MESSAGE)
    await message.delete()
    if audio.file_id:
        await bot.send_audio(
            chat_id=chat_id, audio=audio.file_id,
            caption=AUDIO_MODERATION_MESSAGE.format(title=audio.title, performer=audio.performer, genre=audio.genre),
            reply_markup=get_moderation_keyboard(audio_id=audio_id)
        )


@router.callback_query(IsAdmin(), ModerationCallbackFactory.filter(F.action == Action.decline))
async def decline_button(query: CallbackQuery, state: FSMContext, callback_data: ModerationCallbackFactory):
    audio_id = callback_data.audio_id
    msg = await query.message.answer(MODERATION_DECLINE_MESSAGE,
                                     reply_markup=get_cancel_keyboard(audio_id=audio_id))
    await state.set_state(ModerationStates.decline)
    await state.set_data({
        'audio_id': audio_id,
        'messages_to_delete': [msg.message_id]
    })
    await query.message.delete()


@router.message(IsAdmin(), ModerationStates.decline)
async def decline(message: Message, database: Database, state: FSMContext, bot: Bot):
    chat_id = message.from_user.id
    sdata = await state.get_data()

    audio_id = sdata['audio_id']
    audio = await database.get_audio_by_id(audio_id=audio_id)

    await bot.send_message(chat_id=audio.added_by,
                           text=DECLINE_USER_MESSAGE.format(title=audio.title, reason=message.text))

    local_path = audio.local_path
    if local_path and os.path.exists(local_path):
        os.remove(local_path)

    await database.delete_audio(audio_id=audio_id)

    await state.clear()
    messages_to_delete = sdata['messages_to_delete']
    for msg in messages_to_delete:
        await bot.delete_message(chat_id=chat_id, message_id=msg)

    await message.answer(SUCCESS_DECLINE_MESSAGE)

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
            await message.answer(
                AUDIO_MODERATION_MESSAGE.format(title=audio.title, performer=audio.performer, genre=audio.genre),
                reply_markup=get_moderation_keyboard(audio_id=audio.id)
            )

    await message.delete()


@router.callback_query(IsAdmin(), ModerationCallbackFactory.filter(F.action == Action.accept))
async def accept_button(query: CallbackQuery, database: Database, callback_data: ModerationCallbackFactory, bot: Bot):
    chat_id = query.from_user.id
    audio_id = callback_data.audio_id

    audio = await database.get_audio_by_id(audio_id=audio_id)
    audio.status = 'accepted'
    await database.update_audio(audio)
    await bot.send_message(chat_id=audio.added_by, text=ACCEPT_USER_MESSAGE.format(title=audio.title))
    await query.message.answer(SUCCESS_ACCEPT_MESSAGE)

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

    await query.message.delete()
