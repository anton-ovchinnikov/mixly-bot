from aiogram.fsm.state import StatesGroup, State


class AddAudioStates(StatesGroup):
    title = State()
    performer = State()
