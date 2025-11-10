"""
Pytest file for Lab11_dpatel85.py
Author: Disha Patel
Date: 2025-11-09
"""

import pytest
from Lab11_dpatel85 import normalize_rotation

def test_input_100_returns_100():
    assert normalize_rotation(100) == 100

def test_input_460_returns_100():
    assert normalize_rotation(460) == 100

def test_input_820_returns_100():
    assert normalize_rotation(820) == 100

def test_input_minus_100_returns_260():
    assert normalize_rotation(-100) == 260

def test_input_minus_460_returns_260():
    assert normalize_rotation(-460) == 260

def test_input_minus_820_returns_260():
    assert normalize_rotation(-820) == 260

def test_non_numeric_raises():
    with pytest.raises(TypeError):
        normalize_rotation("invalid")