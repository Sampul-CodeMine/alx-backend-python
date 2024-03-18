#!/usr/bin/env python3
"""
This is a module that contains an async coroutine function that accepts an
integer parameter
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    This is an asynchronous function that waits for a random number of seconds

    Args:
        max_delay (int) - number of delay

    Returns:
        float number
    """
    waiting_time = random.random() * max_delay
    await asyncio.sleep(waiting_time)

    return waiting_time
