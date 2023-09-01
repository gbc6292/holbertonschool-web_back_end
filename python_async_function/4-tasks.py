#!/usr/bin/env python3
"""Function code is nearly identical to
wait_n except task_wait_random is being called."""
import asyncio
from typing import List

# Import the task_wait_random function from the same module.
task_wait_random = __import__('3-tasks import').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous function that generates a list of random delays using tasks.

    Args:
        n (int): The number of random delays to generate.
        max_delay (int): The maximum delay in seconds for each random delay.

    Returns:
        List[float]: A list of random delays as floating-point numbers.
    """
    delay_list: List[float] = []
    tasks: List[asyncio.Task] = []

    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    for completed_task in asyncio.as_completed(tasks):
        delay = await completed_task
        delay_list.append(delay)

    return delay_list

if __name__ == "__main__":
    n = 5
    max_delay = 6

    result = asyncio.run(task_wait_n(n, max_delay))
    print(result)
