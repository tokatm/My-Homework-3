import numpy as np
#import numpy.polymul as npp


x = np.poly1d([1,0,1,0,0,1,0,1])
y = np.poly1d([0,0,0,0,1,1,0,1])
p = np.poly1d([1,0,0,0,1,1,0,1,1])

def inv(x,y):
   k = np.polymul(x,y)
   #res = np.polydiv(k,p)
   quotient, remainder = np.polydiv(k,p)
   list_e = (remainder.coefficients%2)
   print(np.poly1d(list_e))

inv(x,y)
