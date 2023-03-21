from aiogram.fsm.state import StatesGroup, State


class ModerationStates(StatesGroup):
    title = State()
    performer = State()
