from sqlalchemy import Column, Integer, ForeignKey

from orm import Base


class EventParticipant(Base):
    __tablename__ = 'event_participants'
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id'))
    player_id = Column(Integer, ForeignKey('players.id'))
