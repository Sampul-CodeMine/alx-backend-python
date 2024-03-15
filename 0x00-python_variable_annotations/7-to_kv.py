#!/usr/bin/env python3
"""
This is a module for complex typed annotation
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """"
    This is a function that accepts two arguments: one a string, the other
    an int or float and returns a tuple.

    Args:
        k (str): A string parameter
        v (int | float): Either float or integer parameter

    Return:
        (tuple) - A tuple of a string and square of {v}
    """
    return (k, (v * v))
