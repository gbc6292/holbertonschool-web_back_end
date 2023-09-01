#!/usr/bin/env python3
"""Function code is nearly identical to
wait_n except task_wait_random is being called."""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return a list of float ascending order"""
    delay_list: List[float] = []
    tasks: List = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delay_list.append(delay)

    return delay_list
