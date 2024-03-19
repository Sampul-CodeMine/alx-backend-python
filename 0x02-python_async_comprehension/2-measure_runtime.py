#!/usr/bin/env python3
"""
Module Async Coroutine to show runtime for 4 parallel comprehension
Task -1
"""
import asyncio
import time
from importlib import import_module as get


async_comprehension = get('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    This is a function that will execute {async_comprehension} four (4)
    times in parallel using async.gather() method

    Returns:
        float - the time measured to run the parallel routines
    """
    st_tyme = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    return time.time() - st_tyme
