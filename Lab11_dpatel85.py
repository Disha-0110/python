"""
Program: Lab11_dpatel85.py
Author: Disha Patel
Purpose: Normalize a rotation (in degrees) to remove full 360° turns.
Date: 2025-11-09
"""

from typing import Union

Number = Union[int, float]

def normalize_rotation(deg: Number) -> float:
    """
    Normalize degree input to range [0, 360).
    Examples:
        100  -> 100
        460  -> 100
        -100 -> 260
    Raises:
        TypeError: if deg is not int or float
    """
    if not isinstance(deg, (int, float)):
        raise TypeError("deg must be numeric (int or float)")
    return deg % 360