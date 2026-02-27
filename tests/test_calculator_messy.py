import pytest

from app.calculator import add, divide, total


def test_addition_basic():
    r = add(1, 2)
    assert r.value == 3
    assert r.message == "ok"


def test_addition_more_cases():
    r = add(0, 0)
    assert r.value == 0

    r = add(-1, 1)
    assert r.value == 0

    r = add(2.5, 2.5)
    assert r.value == 5.0


def test_divide_ok():
    r = divide(10, 2)
    assert r.value == 5
    assert r.message == "ok"


def test_divide_by_zero_raises():
    with pytest.raises(Exception) as e:
        divide(1, 0)
    assert "zero" in str(e.value).lower()


def test_total_list():
    items = [1, 2, 3]
    t = total(items)
    assert t == 6.0

    items = [0.1, 0.2, 0.3]
    t = total(items)
    assert round(t, 2) == 0.6