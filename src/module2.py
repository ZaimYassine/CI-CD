# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 08:28:21 2024

@author: Yassine Zaim
"""

# =============================================================================
# advanced Calculator
# =============================================================================
import math
import numpy as np
import matplotlib.pyplot as plt

class AdvancedCalculator:
    
    def exp(self, a):
        return math.exp(a)
    
    def power(self, a, n):
        return pow(a, n)
    
    def sqrt(self, a):
        return math.sqrt(a)
        
    def tan(self, a):
        return math.tan(a)
    
    def sin(self, a):
        return math.sin(a)
    
    def plot_fig(self):
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        plt.plot(x, y)
        plt.title("Plot y = f(x)")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()
    
if __name__ == "__main__":
    
    AdvCalc = AdvancedCalculator()
    a = 10
    b = 2
    n = 3
    print(f"The exp of the numbers {a} is: {AdvCalc.exp(a)}")
    print(f"The number {a} power {n} is: {AdvCalc.power(a, n)}")  
    print(f"The sqrt of the numbers {a} is: {AdvCalc.sqrt(a)}")
    print(f"The tan of the numbers {a} is: {AdvCalc.tan(a)}")
    print(f"The sin of the numbers {a} is: {AdvCalc.sin(a)}")
    AdvCalc.plot_fig()