#!/usr/bin/env python3
"""
Module Async Generator - Task 0
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    This is an async function that generates 10 numbers sequentially
    """
    for idx in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
