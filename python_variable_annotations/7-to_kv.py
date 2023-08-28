#!/usr/bin/env python3
"""Type-annotated function to_kv that takes a string k and an
int OR float v as arguments and returns a tuple. The first
element of the tuple is the string k"""

from typing import List, Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    """Return a tuple"""
    return tuple([k, v*v])
