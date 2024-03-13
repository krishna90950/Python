import pytest

@pytest.mark.parametrize("num",[4, 4], [1, 2])
def test_add(num):
    assert num + 2 == 10, "sum is not equal to 10"