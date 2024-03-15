#!/usr/bin/env python3
"""
This is a module for Task 11
"""

from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Function to retrieve a value from the dictionary using a given key
    """
    if key in dct:
        return dct[key]
    return default
