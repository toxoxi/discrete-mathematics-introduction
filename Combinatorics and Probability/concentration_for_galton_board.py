from operator import mul
from fractions import Fraction
from functools import reduce

def nCk(n,k): 
  return int(reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1))

sum = 0
n = 1000
for k in range(400, 601):
  sum += (nCk(n, k) / (2**n))
