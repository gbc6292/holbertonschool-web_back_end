#!/usr/bin/env python3
"""Module that return  a start and end indices for pagination"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """function that calculates the start and end"""

    end_size: int = page * page_size
    start_size: int = end_size - page_size

    return (start_size, end_size)
