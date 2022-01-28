from sqlalchemy import Column, Integer, String, ForeignKey

from orm import Base


class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    user = Column(Integer, ForeignKey('users.id'))
