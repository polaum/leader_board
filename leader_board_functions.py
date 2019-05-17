from create_db import User, Session
from sqlalchemy import desc


class ScoreNotEligible(Exception):
    pass


def add_score(user_name, score, items_shot, time_played):
    if is_score_eligible(score):
        session = Session()
        new_user = User(user_name=user_name, score=score, items_shot=items_shot, time_played=time_played)
        if get_leaders().count() >= 10:
            session.query(User).filter(User.score == _min_score()).delete()
        session.add(new_user)
        session.commit()
        session.close()
    else:
        raise ScoreNotEligible('This score is not good enough to enter the leaders board')


def get_leaders():
    session = Session()
    result = session.query(User).order_by(desc(User.score)).slice(0, 11)
    session.close()
    return result


def is_score_eligible(score: int):
    session = Session()
    lb = get_leaders()
    leader_board_size = lb.count()
    if leader_board_size < 10:
        session.close()
        return True
    elif _min_score() < score:
        session.close()
        return True
    session.close()
    return False


def _min_score():
    lb = get_leaders()
    leader_board_size = lb.count()
    return int(lb[leader_board_size-1].score)








