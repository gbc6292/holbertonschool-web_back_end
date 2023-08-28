#!/usr/bin/env python3
"""Type-annotated function to_str that takes a float n
as argument and returns the string representation of the float"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the result of a list sum"""
    a = sum(input_list)
    return a
