from typing import Any

from .ops import mul


def double(value: Any) -> Any:
    return mul(value, 2)


def triple(value: Any) -> Any:
    return mul(value, 3)
