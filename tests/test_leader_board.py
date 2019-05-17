import pytest
from leader_board_functions import ScoreNotEligible, add_score, _min_score, get_leaders


def test_add_new_score_not_eligible():
    with pytest.raises(ScoreNotEligible):
        add_score('falula', 1, 0, 12.45)


def test_add_new_score_eligible():
    current_min_score = _min_score()
    add_score('falula', 100, 0, 12.45)
    assert get_leaders().count <= 10
    assert current_min_score != _min_score()

