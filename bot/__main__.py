import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram import F
from aiogram.fsm.storage.memory import MemoryStorage
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from bot.configreader import config
from bot.database.Database import Database
from bot.database.base import Base
from bot.handlers import menuHandlers, profileHandlers, audioHandlers, adminHandlers, moderationHandlers, \
    catalogHandlers, loaderHandlers
from bot.middlewares.DBMiddleware import DBMiddleware


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s - %(levelname)s] %(name)s: %(message)s",
    )

    engine = create_async_engine(f"sqlite+aiosqlite:///database.sqlite", future=True, echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    session_maker = async_sessionmaker(engine, expire_on_commit=False)
    pool = session_maker.begin().async_session
    database = Database(pool=pool)

    bot = Bot(token=config.bot_token, parse_mode="HTML")
    await bot.delete_webhook(drop_pending_updates=True)
    dp = Dispatcher(storage=MemoryStorage())

    dp.message.filter(F.chat.type == "private")

    dp.message.middleware(DBMiddleware(database=database))
    dp.callback_query.middleware(DBMiddleware(database=database))

    dp.include_router(menuHandlers.router)
    dp.include_router(profileHandlers.router)
    dp.include_router(audioHandlers.router)
    dp.include_router(adminHandlers.router)
    dp.include_router(moderationHandlers.router)
    dp.include_router(catalogHandlers.router)
    dp.include_router(loaderHandlers.router)

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await dp.storage.close()
        await pool.close()
        await engine.dispose()
        await bot.session.close()


asyncio.run(main())
