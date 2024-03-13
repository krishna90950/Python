import pytest

a = 10
b = 0

@pytest.mark.skip()
def test_addition():
    assert a + b != 0, "sum of a plu b is zero"


# Mark tests as "addition"
@pytest.mark.skipif(b==0, "zero multi")
def test_multiplication():
    assert a * b, "sB is greater than a"