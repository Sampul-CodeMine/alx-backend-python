#!/usr/bin/env python3
"""
This is a module to define complex types [list of union of floats]
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This is a function that sums all the elements of a list of floats

    Args:
        mxd_lst: List[Union[float]]

    Return:
        (float) sum of all the float elements in the list
    """
    total: float = 0.0
    for i in mxd_lst:
        total += i
    return total
