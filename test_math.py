import pytest


@pytest.fixture
def s_list():
    return [1, 2, 3, 4]


def test_max(s_list):
    assert max([1, 2, 3, 4]) == 4




def test_sum(s_list):
    assert sum([1, 2, 3, 4]) == 10
