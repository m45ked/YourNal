from sqlalchemy import Column, Integer, ForeignKey, String

from orm import Base


class EventNote(Base):
    __tablename__ = 'event_notes'
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'))
    note = Column(String, nullable=False)
