from sympy import gcdex
from sympy.abc import x

print(gcdex(x+1, x**8 + x**4 + x**3 + x + 1))