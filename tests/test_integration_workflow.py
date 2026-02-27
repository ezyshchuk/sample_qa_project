import pytest

from app.auth import User, login
from app.calculator import add, divide, total


@pytest.fixture()
def user():
    return User(username="bob", password="builder")


def compute_score(values: list[float]) -> float:
    base = total(values)
    bonus = add(base, 1).value
    return divide(bonus, 2).value


def test_user_can_login_and_compute_score(user):
    token = login(user, "bob", "builder")
    assert token

    score = compute_score([1, 2, 3])
    assert score == 3.5


def test_compute_score_with_decimals():
    score = compute_score([0.1, 0.2, 0.3])
    assert round(score, 2) == 0.8