from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CalcResult:
    value: float
    message: str = ""


def add(a: float, b: float) -> CalcResult:
    return CalcResult(value=a + b, message="ok")


def divide(a: float, b: float) -> CalcResult:
    if b == 0:
        raise ZeroDivisionError("b must not be zero")
    return CalcResult(value=a / b, message="ok")


def total(items: list[float]) -> float:
    s = 0.0
    for x in items:
        s += float(x)
    return s