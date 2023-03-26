import os

from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import FSInputFile, Message
from mutagen.id3 import ID3, ID3NoHeaderError

from bot.database.Database import Database
from bot.filters.IsAdmin import IsAdmin

router = Router()


@router.message(IsAdmin(), Command('loader'))
async def loader_cmd(message: Message, bot: Bot, database: Database):
    await message.answer(text='<b>Началась загрузка аудио!</b>')

    filenames = os.listdir('loader/')
    for n, filename in enumerate(filenames):
        audio_name = filename.split('.mp3')[0]
        performer, title = audio_name.split(' - ')

        audio = None
        try:
            audio = ID3(f'loader/{filename}')
            audio.delete()
        except ID3NoHeaderError:
            pass

        audio = FSInputFile(f'loader/{filename}')

        msg = await bot.send_audio(chat_id=message.from_user.id, audio=audio)
        await database.add_audio(added_by=message.from_user.id, title=title,
                                 performer=performer)
        audio = await database.get_audio_by_title(title=title)
        audio.local_path = f'music/{msg.audio.file_id}.mp3'
        audio.file_id = msg.audio.file_id
        await database.update_audio(audio)

        os.rename(f'loader/{filename}', f'music/{msg.audio.file_id}.mp3')

        await message.answer(text=f'<b>{n + 1}/{len(filenames)}</b>')

    await message.answer(text='<b>Загрузка аудио закончена!</b>')
