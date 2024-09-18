# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 11:34:46 2024

@author: Yassine Zaim
"""
import pytest
import sys
import os

print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import module3 as mod3

# =============================================================================
# Test Module3
# =============================================================================

def test_show():
    ShowCl = mod3.ShowClass()
    assert ShowCl.show() == "I am the function show from the ShowClass"


