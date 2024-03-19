#!/usr/bin/env python3
"""
Module Async Comprehension - Task 1
"""
from typing import List
from importlib import import_module as get


async_generator = get('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    This is an async function that generates 10 numbers sequentially
    using async comprehension
    """
    return [n async for n in async_generator()]
