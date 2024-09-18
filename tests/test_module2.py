# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 11:30:53 2024

@author: Yassine Zaim
"""

import pytest
import sys
import os

print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import module2 as mod2

# =============================================================================
# Test Module2
# =============================================================================

@pytest.fixture
def sample_data():
    a = 10
    b = 2
    n = 3
    return a, b, n


def test_exp(sample_data):
    a, b, n = sample_data
    print(f"a = {a}, b = {b} and n = {n}")
    AdvCalc = mod2.AdvancedCalculator()
    assert round(AdvCalc.exp(a), 2) == 22026.47
    
def test_power(sample_data):
    a, b, n = sample_data
    print(f"a = {a}, b = {b} and n = {n}")
    AdvCalc = mod2.AdvancedCalculator()
    assert AdvCalc.power(a, n) == 1000

def test_sqrt(sample_data):
    a, b, n = sample_data
    print(f"a = {a}, b = {b} and n = {n}")
    AdvCalc = mod2.AdvancedCalculator()
    assert round(AdvCalc.sqrt(a), 2) == 3.16

def test_tan(sample_data):
    a, b, n = sample_data
    print(f"a = {a}, b = {b} and n = {n}")
    AdvCalc = mod2.AdvancedCalculator()
    assert round(AdvCalc.tan(a), 2) == 0.65
