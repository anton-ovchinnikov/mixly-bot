from dataclasses import dataclass
from os import getenv

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    bot_token: str = getenv('BOT_TOKEN')
    admin_id: int = int(getenv('ADMIN_ID'))


config = Config()
