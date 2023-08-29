#!/usr/bin/env python3
"""Type-annotated function make_multiplier that takes a
float multiplier as argument and returns a function that
multiplies a float by multiplier"""

from typing import Callable, Union


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creating a multiplier method"""
    def multiplier_function(a: float) -> float:
        """Get the multiplier"""
        return a * multiplier
    return multiplier_function
