#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument (max_delay
with a default value of 10) named wait_random that waits for a random
delay between 0 and max_delay (included and float value) seconds and
eventually returns i"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that generates a random delay between
    0 and max_delay seconds (inclusive).

    Args:
        max_delay (int, optional): The maximum delay in seconds.
        Defaults to 10.

    Returns:
        float: A random delay in seconds as a floating-point number.
    """
    random_delay = random.uniform(0, max_delay)

    await asyncio.sleep(random_delay)
    return random_delay
