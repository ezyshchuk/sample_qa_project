import pytest

from app.auth import AuthError, User, login


@pytest.fixture()
def demo_user():
    return User(username="alice", password="wonderland")


def test_login_success_returns_token(demo_user):
    token = login(demo_user, "alice", "wonderland")
    assert isinstance(token, str)
    assert len(token) > 0


def test_login_bad_password(demo_user):
    with pytest.raises(AuthError):
        login(demo_user, "alice", "WRONG")


def test_login_token_is_stable_for_same_credentials(demo_user):
    t1 = login(demo_user, "alice", "wonderland")
    t2 = login(demo_user, "alice", "wonderland")
    assert t1 == t2  # intentionally wrong