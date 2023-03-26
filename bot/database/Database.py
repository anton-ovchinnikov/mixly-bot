import datetime

from sqlalchemy import select, delete
from sqlalchemy.dialects.sqlite import insert
from sqlalchemy.ext.asyncio import AsyncSession

from bot.database.models import User, Audio


class Database:
    def __init__(self, pool: AsyncSession):
        self.pool = pool

    async def add_user(self, chat_id: int, username: str):
        values = {'chat_id': chat_id, 'username': username, 'registered_at': datetime.datetime.now()}

        stmt = insert(User).values(**values).on_conflict_do_nothing()
        await self.pool.execute(stmt)
        await self.pool.commit()

    async def get_user(self, chat_id: int):
        stmt = select(User).where(User.chat_id == chat_id)
        user = await self.pool.execute(stmt)
        return user.scalar_one_or_none()

    async def add_audio(self, title: str, performer: str, added_by: int):
        self.pool.add(Audio(title=title, performer=performer, added_by=added_by))
        await self.pool.commit()

    async def get_audios(self):
        stmt = select(Audio).where(Audio.status == 'accepted').order_by(Audio.id.asc()).limit(10)
        audios = await self.pool.execute(stmt)
        return audios.scalars()

    async def get_audios_count(self):
        stmt = select(Audio).where(Audio.status == 'accepted').order_by(Audio.id.asc())
        audios = await self.pool.execute(stmt)
        audios = audios.scalars()
        count = len([audio for audio in audios])
        return count

    async def get_offset_audios(self, offset: int):
        stmt = select(Audio).where(Audio.status == 'accepted').order_by(Audio.id.asc()).offset(offset).limit(10)
        audios = await self.pool.execute(stmt)
        return audios.scalars()

    async def get_audio_by_id(self, audio_id: int):
        stmt = select(Audio).where(Audio.id == audio_id).order_by(Audio.id.asc())
        audio = await self.pool.execute(stmt)
        return audio.scalar_one_or_none()

    async def get_audio_by_title(self, title: str):
        stmt = select(Audio).where(Audio.title == title).order_by(Audio.id.asc())
        audio = await self.pool.execute(stmt)
        return audio.scalar_one_or_none()

    async def get_audio_for_moderation(self):
        status = 'pending'
        stmt = select(Audio).where(Audio.status == status).order_by(Audio.id.asc()).limit(1)
        audio = await self.pool.execute(stmt)
        return audio.scalar_one_or_none()

    async def update_audio(self, audio: Audio):
        self.pool.add(audio)
        await self.pool.commit()

    async def delete_audio(self, audio_id: int):
        stmt = delete(Audio).where(Audio.id == audio_id)
        await self.pool.execute(stmt)
        await self.pool.commit()
