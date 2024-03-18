#!/usr/bin/env python3
"""
This is a module that performs async task using regular function
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    This is a function that creates an async coroutine

    Args:
        max_delay (int)

    Returns:
        Async task
    '''
    return asyncio.create_task(wait_random(max_delay))
