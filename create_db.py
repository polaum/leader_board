from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://localhost:5433/leader_board')
Base = declarative_base()
Session = sessionmaker(bind=engine)


class User(Base):
    __tablename__ = 'leader_board'
    user_name = Column(String, primary_key=True)
    score = Column(Integer)
    items_shot = Column(Integer)
    time_played = Column(Float)

    def __repr__(self):
        return "<User(user_name='%s', score='%s', items_shot='%s', time_played='%s)>" % \
               (self.user_name, self.score, self.items_shot, self.time_played)

