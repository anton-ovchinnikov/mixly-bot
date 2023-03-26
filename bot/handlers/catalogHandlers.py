from aiogram import Router, F, Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from bot.callbacks.CatalogPaginationCallbackFactory import CatalogPaginationCallbackFactory, Action
from bot.database.Database import Database
from bot.keyboards.catalogKeyboards import get_catalog_pagination_keyboard
from bot.keyboards.menuKeyboard import get_menu_keyboard
from bot.labels.messageLabels import FIRST_CATALOG_MESSAGE, AUDIO_CATALOG_MESSAGE, SECOND_CATALOG_MESSAGE, START_MESSAGE
from bot.states.CatalogStates import CatalogStates

router = Router()


@router.callback_query(CatalogStates.catalog, CatalogPaginationCallbackFactory.filter(F.action == Action.next))
async def next_button(query: CallbackQuery, callback_data: CatalogPaginationCallbackFactory, bot: Bot,
                      database: Database, state: FSMContext):
    chat_id = query.from_user.id
    offset = callback_data.offset
    audios = await database.get_offset_audios(offset=offset)

    messages_to_delete = await state.get_data()
    messages_to_delete = messages_to_delete['messages_to_delete']
    for message_id in messages_to_delete:
        await bot.delete_message(chat_id=chat_id, message_id=message_id)

    messages_to_delete = []
    msg = await query.message.answer(text=FIRST_CATALOG_MESSAGE)
    messages_to_delete.append(msg.message_id)

    for audio in audios:
        msg = await bot.send_audio(
            chat_id=chat_id, audio=audio.file_id,
            caption=AUDIO_CATALOG_MESSAGE.format(title=audio.title, performer=audio.performer)
        )
        messages_to_delete.append(msg.message_id)

    await state.set_data({'messages_to_delete': messages_to_delete})

    audios_count = await database.get_audios_count()
    is_max_offset = False
    if offset + 10 > audios_count:
        is_max_offset = True
    await query.message.answer(
        text=SECOND_CATALOG_MESSAGE,
        reply_markup=get_catalog_pagination_keyboard(offset=offset, is_max_offset=is_max_offset)
    )
    await query.message.delete()


@router.callback_query(CatalogStates.catalog, CatalogPaginationCallbackFactory.filter(F.action == Action.back))
async def back_button(query: CallbackQuery, callback_data: CatalogPaginationCallbackFactory, bot: Bot,
                      database: Database, state: FSMContext):
    chat_id = query.from_user.id
    offset = callback_data.offset
    audios = await database.get_offset_audios(offset=offset)

    messages_to_delete = await state.get_data()
    messages_to_delete = messages_to_delete['messages_to_delete']
    for message_id in messages_to_delete:
        await bot.delete_message(chat_id=chat_id, message_id=message_id)

    messages_to_delete = []
    msg = await query.message.answer(text=FIRST_CATALOG_MESSAGE)
    messages_to_delete.append(msg.message_id)

    for audio in audios:
        msg = await bot.send_audio(
            chat_id=chat_id, audio=audio.file_id,
            caption=AUDIO_CATALOG_MESSAGE.format(title=audio.title, performer=audio.performer)
        )
        messages_to_delete.append(msg.message_id)

    await state.set_data({'messages_to_delete': messages_to_delete})
    await query.message.answer(text=SECOND_CATALOG_MESSAGE, reply_markup=get_catalog_pagination_keyboard(offset=offset))
    await query.message.delete()


@router.callback_query(CatalogStates.catalog, CatalogPaginationCallbackFactory.filter(F.action == Action.close))
async def close_button(query: CallbackQuery, bot: Bot, state: FSMContext):
    chat_id = query.from_user.id

    messages_to_delete = await state.get_data()
    messages_to_delete = messages_to_delete['messages_to_delete']
    for message_id in messages_to_delete:
        try:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
        except TelegramBadRequest:
            pass

    await state.clear()
    await query.message.answer(text=START_MESSAGE, reply_markup=get_menu_keyboard())
    await query.message.delete()
