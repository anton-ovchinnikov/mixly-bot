from aiogram import Router, F, Bot
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from bot.database.Database import Database
from bot.keyboards.catalogKeyboards import get_catalog_pagination_keyboard
from bot.keyboards.menuKeyboard import get_menu_keyboard
from bot.keyboards.profileKeyboard import get_profile_keyboard
from bot.labels.buttonLabels import PROFILE_BUTTON, SUPPORT_BUTTON, CATALOG_BUTTON
from bot.labels.messageLabels import START_MESSAGE, INDEV_MESSAGE, PROFILE_MESSAGE, FIRST_CATALOG_MESSAGE, \
    AUDIO_CATALOG_MESSAGE, SECOND_CATALOG_MESSAGE
from bot.states.CatalogStates import CatalogStates

router = Router()


@router.message(CommandStart())
async def start_command(message: Message, database: Database):
    await database.add_user(chat_id=message.from_user.id, username=message.from_user.username)
    await message.answer(START_MESSAGE, reply_markup=get_menu_keyboard())
    await message.delete()


@router.message(F.text == CATALOG_BUTTON)
async def catalog_button(message: Message, database: Database, bot: Bot, state: FSMContext):
    chat_id = message.from_user.id
    audios = await database.get_audios()
    messages_to_delete = []
    await state.set_state(CatalogStates.catalog)

    msg = await message.answer(text=FIRST_CATALOG_MESSAGE, reply_markup=ReplyKeyboardRemove())
    messages_to_delete.append(msg.message_id)

    for audio in audios:
        msg = await bot.send_audio(
            chat_id=chat_id, audio=audio.file_id,
            caption=AUDIO_CATALOG_MESSAGE.format(title=audio.title, performer=audio.performer)
        )
        messages_to_delete.append(msg.message_id)

    await state.set_data({'messages_to_delete': messages_to_delete})

    await message.answer(
        text=SECOND_CATALOG_MESSAGE, reply_markup=get_catalog_pagination_keyboard()
    )
    await message.delete()


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
