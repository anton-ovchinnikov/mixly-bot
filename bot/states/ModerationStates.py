from aiogram.fsm.state import StatesGroup, State


class ModerationStates(StatesGroup):
    title = State()
    performer = State()
    audio_file = State()
