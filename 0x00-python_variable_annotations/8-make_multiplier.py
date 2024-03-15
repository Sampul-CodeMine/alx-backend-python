#!/usr/bin/env python3
"""
This is a module for complex typed function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """"
    This is a function that accepts a float as an argument and returns
    a function that multiplies a float by the variable {multiplier}

    Args:
        multiplier (float): Multiplier argument

    Return:
        callable function.
    """
    def mult(x: float) -> float:
        return x * multiplier
    return mult
