from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import DB_URL

engine = create_engine(DB_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'leader_board'
    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    score = Column(Integer)
    items_shot = Column(Integer)
    time_played = Column(Float)

    def __repr__(self):
        return "<User(user_name='%s', score='%s', items_shot='%s', time_played='%s)>" % \
               (self.user_name, self.score, self.items_shot, self.time_played)

