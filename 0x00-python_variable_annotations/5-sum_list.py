#!/usr/bin/env python3
"""
This is a module to define complex types [list of floats]
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This is a function that sums all the elements of a list of floats

    Args:
        input_list: List[float]

    Return:
        (float) sum of all the float elements in the list
    """
    total: float = 0.0
    for i in input_list:
        total += i
    return total
