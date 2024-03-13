import pytest

a = 10
b = 5
@pytest.mark.addition
def test_addition():
    assert a + b != 0, "sum of a plu b is zero"


# Mark tests as "addition"
@pytest.mark.addition
def test_subtraction():
    assert a > b, "sB is greater than a"

@pytest.mark.multiplication
def test_multiplication():
    assert a * b != 0, " multiplication value is zero"

@pytest.mark.Division
def test_division():
    assert a/b == 1, " multiplication value is zero"

