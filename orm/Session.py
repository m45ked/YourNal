from sqlalchemy import Column, Integer, Date, ForeignKey

from orm import Base


class Session(Base):
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    campaign_id = Column(Integer, ForeignKey('campaigns.id'))
    gm_id = Column(Integer, ForeignKey('users.id'))
