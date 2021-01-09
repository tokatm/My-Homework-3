import numpy as np


m = input("değer gir: ").split(',')
s = input("ikinci gir: ").split(',')

x = np.poly1d(list(map(int, m)))
y = np.poly1d(list(map(int, s)))
p = np.poly1d([1,0,0,0,1,1,0,1,1])


def inv(x,y):
   k = np.polymul(x,y)
   #res = np.polydiv(k,p)
   quotient, remainder = np.polydiv(k,p)
   list_e = (remainder.coefficients % 2)
   print(np.poly1d(list_e))

inv(x,y)
