import logging

import pytest

from app.calculator import add, divide, total


logger = logging.getLogger(__name__)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 1, 0),
        (2.5, 2.5, 5.0),
    ],
)
def test_addition_cases(a, b, expected):
    logger.info("Adding %s and %s", a, b)
    result = add(a, b)
    logger.info("Validating add result")
    assert result.value == expected
    assert result.message == "ok"


def test_divide_ok():
    logger.info("Dividing %s by %s", 10, 2)
    result = divide(10, 2)
    logger.info("Validating divide result")
    assert result.value == 5
    assert result.message == "ok"


def test_divide_by_zero_raises():
    logger.info("Validating divide by zero error path")
    with pytest.raises(ZeroDivisionError, match="b must not be zero") as exc_info:
        divide(1, 0)
    assert str(exc_info.value) == "b must not be zero"


@pytest.mark.parametrize(
    "items,expected",
    [
        ([1, 2, 3], 6.0),
        ([0.1, 0.2, 0.3], 0.6),
    ],
)
def test_total_list(items, expected):
    logger.info("Summing items: %s", items)
    result = total(items)
    logger.info("Validating total result")
    assert result == pytest.approx(expected)