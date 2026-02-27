import logging

import pytest

from app.auth import AuthError, User, login


logger = logging.getLogger(__name__)


def _mask_token(token: str) -> str:
    if not token:
        return "<empty>"
    if len(token) <= 6:
        return f"{token[:1]}***"
    return f"{token[:3]}***{token[-3:]}"


@pytest.fixture()
def demo_user():
    logger.info("setup demo user username=%s", "alice")
    return User(username="alice", password="wonderland")


def test_login_success_returns_token(demo_user):
    logger.info("action login attempt username=%s", "alice")
    token = login(demo_user, "alice", "wonderland")
    logger.info("result token issued token=%s", _mask_token(token))
    assert isinstance(token, str)
    assert len(token) > 0


def test_login_bad_password(demo_user):
    logger.info("action login attempt with invalid password username=%s", "alice")
    with pytest.raises(AuthError):
        login(demo_user, "alice", "WRONG")
    logger.info("result login rejected username=%s", "alice")


def test_login_token_is_stable_for_same_credentials(demo_user):
    logger.info("action first login attempt username=%s", "alice")
    t1 = login(demo_user, "alice", "wonderland")
    logger.info("result first token token=%s", _mask_token(t1))
    logger.info("action second login attempt username=%s", "alice")
    t2 = login(demo_user, "alice", "wonderland")
    logger.info("result second token token=%s", _mask_token(t2))
    assert t1 == t2  # intentionally wrong