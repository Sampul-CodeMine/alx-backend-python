#!/usr/bin/env python3
"""
This is a module that gets runtime for an async coroutine
"""
import asyncio
import time as tym


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    This is a function that computes the time for a corotine wait

    Args:
        n (int)
        max_delay (int)

    Returns:
        float number
    """
    st_time = tym.time()
    asyncio.run(wait_n(n, max_delay))

    return (tym.time() - st_time) / n
