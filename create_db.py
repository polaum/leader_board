from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float
engine = create_engine('postgresql://localhost:5433/leader_board')
meta = MetaData()

leader_board = Table(
    'leader_board', meta,
    Column('user_name', String, primary_key=True),
    Column('score', Integer),
    Column('items_shot', Integer),
    Column('time_played', Float),
)

meta.create_all(engine)