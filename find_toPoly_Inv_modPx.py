from sympy import gcdex
from sympy.abc import x

print(gcdex(x**6 + x**3 + x, x**8 + x**4 + x**3 + x + 1))