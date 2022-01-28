from sqlalchemy import Column, Integer, String

from orm import Base


class Campaign(Base):
    __tablename__ = 'campaigns'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    desc = Column(String)
