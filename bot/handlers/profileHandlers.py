from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from bot.callbacks.ProfileCallbackFactory import ProfileCallbackFactory, Action
from bot.keyboards.profileKeyboard import get_cancel_keyboard
from bot.labels.messageLabels import ADD_AUDIO_TITLE_MESSAGE, CANCEL_MESSAGE
from bot.states.AddAudioStates import AddAudioStates

router = Router()


@router.callback_query(ProfileCallbackFactory.filter(F.action == Action.add_audio))
async def add_audio_callback(query: CallbackQuery, state: FSMContext):
    msg = await query.message.answer(ADD_AUDIO_TITLE_MESSAGE,
                                     reply_markup=get_cancel_keyboard(chat_id=query.from_user.id))
    await query.message.delete()
    await state.set_state(AddAudioStates.title)
    await state.set_data({'messages_to_delete': [msg.message_id]})
    await query.answer()


@router.callback_query(ProfileCallbackFactory.filter(F.action == Action.cancel))
async def cancel(query: CallbackQuery, state: FSMContext, bot: Bot):
    sdata = await state.get_data()

    await state.clear()
    await query.message.answer(CANCEL_MESSAGE)

    chat_id = query.from_user.id
    messages_to_delete = sdata['messages_to_delete']
    for msg in messages_to_delete:
        await bot.delete_message(chat_id=chat_id, message_id=msg)
    await query.answer()
