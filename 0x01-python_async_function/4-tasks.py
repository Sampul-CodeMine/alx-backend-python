#!/usr/bin/env python3
"""
This is a module that contains multiple async coroutine function
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    This is a function that executes multiple routines at the same time

    Args:
        n (int)
        max_deley (int)

    Returns:
        list(float) - A list of float numbers
    """
    waiting_time = await asyncio.gather(*tuple(
        map(lambda _: task_wait_random(max_delay), range(n))))
    return sorted(waiting_time)
