# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 08:28:21 2024

@author: Yassine Zaim
"""

# =============================================================================
# advanced Calculator
# =============================================================================
import math

class AdvancedCalculator:
    
    def exp(self, a):
        return math.exp(a)
    
    def power(self, a, n):
        return pow(a, n)
    
    def sqrt(self, a):
        return math.sqrt(a)
        
    
if __name__ == "__main__":
    
    AdvCalc = AdvancedCalculator()
    a = 10
    b = 2
    n = 3
    print(f"The exp of the numbers {a} is: {AdvCalc.exp(a)}")
    print(f"The number {a} power {n} is: {AdvCalc.power(a, n)}")  
    print(f"The sqrt of the numbers {a} is: {AdvCalc.sqrt(a)}")

    