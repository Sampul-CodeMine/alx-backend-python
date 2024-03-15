#!/usr/bin/env python3
"""
This is a module for duck typing
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """"
    This is a function that returns values with appropriate types

    Args:
        lst (Iterable[Sequence])

    Return:
        List of Tuples with sequence of integers
    """
    return [(i, len(i)) for i in lst]
