from sqlalchemy import Column, Integer, String, ForeignKey

from orm import Base


class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    session_id = Column(Integer, ForeignKey('sessions.id'))
