#!/usr/bin/env python3
'''
takes in 2 int arguments (in this order): n and max_delay
return the list of all the delays (float values).
'''
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous function that generates a list of random delays.

    Args:
        n (int): The number of random delays to generate.
        max_delay (int): The maximum delay in seconds for each random delay.

    Returns:
        List[float]: A list of random delays as floating-point numbers.
    """
    delay_list: List[float] = []
    task: float = []

    for _ in range(n):
        task.append(wait_random(max_delay))

    for task in asyncio.as_completed((task)):
        delay = await task
        delay_list.append(delay)
    return delay_list
