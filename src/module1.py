# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 08:25:10 2024

@author: Yassine Zaim
"""

# =============================================================================
# Simple Calculator
# =============================================================================

class SimpleCalculator:
    
    def add(self, a, b):
        return a + b
    
    def substract(self, a, b):
        return a - b
    
    def division(self, a, b):
        return a/b
    
    def multiply(self, a, b):
        return a*b
        
    
if __name__ == "__main__":
    
    SimpCalc = SimpleCalculator()
    a = 10
    b = 2
    print(f"The sum of the numbers {a} and {b} is: {SimpCalc.add(a, b)}")
    print(f"The substraction of the numbers {a} and {b} is: {SimpCalc.substract(a, b)}")  
    print(f"The division of the numbers {a} and {b} is: {SimpCalc.division(a, b)}")
    print(f"The multiplication of the numbers {a} and {b} is: {SimpCalc.multiply(a, b)}")
    