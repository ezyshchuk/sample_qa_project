import logging

import pytest

from app.auth import User, login
from app.calculator import add, divide, total


logger = logging.getLogger(__name__)


def _mask_token(token: str) -> str:
    if not token:
        return "<empty>"
    if len(token) <= 6:
        return f"{token[:1]}***"
    return f"{token[:3]}***{token[-3:]}"


@pytest.fixture()
def user():
    logger.info("setup integration user username=%s", "bob")
    return User(username="bob", password="builder")


def compute_score(values: list[float]) -> float:
    logger.info("action compute score input_count=%s", len(values))
    base = total(values)
    logger.info("result total base=%s", base)
    bonus = add(base, 1).value
    logger.info("result bonus bonus=%s", bonus)
    logger.info("action divide bonus by denominator=%s", 2)
    return divide(bonus, 2).value


def test_user_can_login_and_compute_score(user):
    logger.info("action login attempt username=%s", "bob")
    token = login(user, "bob", "builder")
    logger.info("result token issued token=%s", _mask_token(token))
    assert token

    logger.info("action compute score for integer inputs")
    score = compute_score([1, 2, 3])
    logger.info("result computed score=%s", score)
    assert score == 3.5


def test_compute_score_with_decimals():
    logger.info("action compute score for decimal inputs")
    score = compute_score([0.1, 0.2, 0.3])
    logger.info("result computed rounded score=%s", round(score, 2))
    assert round(score, 2) == 0.8