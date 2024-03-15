#!/usr/bin/env python3
"""
This is a module to augument function definition using duck-typed annotations
"""
from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Function to get the datatype of the first element of list of any type

    Args:
        lst (list): A list of any datatype

    Return:
        Nothing or the first element in the list of any datatype
    """
    if lst:
        return lst[0]
    return None
