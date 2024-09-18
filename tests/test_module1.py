# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 09:38:03 2024

@author: Yassine Zaim
"""
import pytest
import sys
import os

print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import module1 as mod1

# =============================================================================
# Test module1
# =============================================================================*

@pytest.fixture
def sample_data():
    a = 10
    b = 2
    n = 3
    return a, b, n


def test_add(sample_data):
    a, b, n = sample_data
    print(f"a = {a}, b = {b} and n = {n}")
    SimpCalc = mod1.SimpleCalculator()
    assert SimpCalc.add(a, b) == 12
    
def test_substract(sample_data):
    a, b, n = sample_data
    print(f"a = {a}, b = {b} and n = {n}")
    SimpCalc = mod1.SimpleCalculator()
    assert SimpCalc.substract(a, b) == 8

def test_division(sample_data):
    a, b, n = sample_data
    print(f"a = {a}, b = {b} and n = {n}")
    SimpCalc = mod1.SimpleCalculator()
    assert SimpCalc.division(a, b) == 5

def test_multiply(sample_data):
    a, b, n = sample_data
    print(f"a = {a}, b = {b} and n = {n}")
    SimpCalc = mod1.SimpleCalculator()
    assert SimpCalc.multiply(a, b) == 20    
    

