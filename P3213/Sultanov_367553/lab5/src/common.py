from typing import Callable

Function = Callable[[float], float]
Checker = Callable[[float], bool]

PRECISION = 6
EPS = 0.000001


def rounded(n: float) -> float:
    return round(n, PRECISION)
