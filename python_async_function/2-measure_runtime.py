#!/usr/bin/env python3
"""Function with integers n and max_delay as
arguments that measures the total execution time
for wait_n(n, max_delay), and returns total_time / n.
Your function should return a float."""
import asyncio
import time
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time of wait_n(n, max_delay).

    Args:
        n (int): The number of random delays to generate.
        max_delay (int): The maximum delay in seconds for each random delay.

    Returns:
        float: The average execution time in seconds.
    """
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n


if __name__ == "__main__":
    n = 5
    max_delay = 9

    avg_execution_time = measure_time(n, max_delay)
    print(avg_execution_time)
