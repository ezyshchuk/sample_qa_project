from __future__ import annotations

import secrets
from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    username: str
    password: str  # demo-only; in real life, passwords should be hashed and salted


class AuthError(ValueError):
    pass


def issue_token(user: User) -> str:
    return secrets.token_hex(8)


def login(user: User, username: str, password: str) -> str:
    if username != user.username:
        raise AuthError("unknown user")
    if password != user.password:
        raise AuthError("bad password")
    return issue_token(user)