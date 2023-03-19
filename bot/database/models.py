from sqlalchemy import Column, BigInteger, Integer, Text, DateTime

from bot.database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    chat_id = Column(BigInteger, unique=True, nullable=False)
    username = Column(Text, unique=True, nullable=True)
    registered_at = Column(DateTime)


class Audio(Base):
    __tablename__ = "audios"

    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False, unique=True)
    author = Column(Text, nullable=False, unique=False)
    genre = Column(Text, nullable=True)
    file_id = Column(Text, unique=True, nullable=True)
    local_path = Column(Text, unique=True, nullable=True)
    added_by = Column(BigInteger, nullable=False)
    moderated_by = Column(BigInteger, nullable=True)
    status = Column(Text, nullable=False, default='pending')
