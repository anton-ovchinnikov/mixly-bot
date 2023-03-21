from aiogram import Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.database.Database import Database
from bot.keyboards.profileKeyboard import get_cancel_keyboard
from bot.labels.messageLabels import ADD_AUDIO_PERFORMER_MESSAGE, SUCCESSFUL_ADD_AUDIO_MESSAGE, \
    AUDIO_ALREADY_EXIST_MESSAGE
from bot.states.AddAudioStates import AddAudioStates

router = Router()


@router.message(AddAudioStates.title)
async def add_audio_title(message: Message, state: FSMContext, bot: Bot, database: Database):
    title = message.text

    sdata = await state.get_data()
    if await database.get_audio_by_title(title=title) is None:
        msg = await message.answer(ADD_AUDIO_PERFORMER_MESSAGE,
                                   reply_markup=get_cancel_keyboard(chat_id=message.from_user.id))
        sdata['messages_to_delete'].append(msg.message_id)
        sdata['title'] = title

        await state.set_data(sdata)
        await state.set_state(AddAudioStates.performer)
    else:
        await state.clear()
        await message.answer(AUDIO_ALREADY_EXIST_MESSAGE)

        chat_id = message.from_user.id
        messages_to_delete = sdata['messages_to_delete']
        for msg in messages_to_delete:
            await bot.delete_message(chat_id=chat_id, message_id=msg)


@router.message(AddAudioStates.performer)
async def add_audio_performer(message: Message, state: FSMContext, bot: Bot, database: Database):
    sdata = await state.get_data()
    messages_to_delete = sdata['messages_to_delete']

    chat_id = message.from_user.id
    title = sdata['title']
    performer = message.text
    await database.add_audio(title=title, performer=performer, added_by=chat_id)

    await state.clear()
    await message.answer(SUCCESSFUL_ADD_AUDIO_MESSAGE)
    for msg in messages_to_delete:
        await bot.delete_message(chat_id=chat_id, message_id=msg)
