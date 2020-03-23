# assumes that p is a permutation of some length (positive) and returns True for even permutations and False for odd ones.
# (The permutation itself should be left unchanged)

def is_even(p):
  a = p[:]
  n = len(a)
  sign = 0 # the number of transpositions mod 2
  s = -1 # first indices are at right places
  while s < n-1:
    u = s+1
    t = u # a[t] is minimal among a[s+1]..a[u]
    while u < n-1:
      u = u+1
      if a[u] < a[t]:
        t = u

    if a[t] != a[s+1]:
      a[s+1], a[t] = a[t], a[s+1]
      sign = 1-sign

    s = s+1

  return True if sign == 0 else False

result = is_even([7, 10, 1, 8, 4, 3, 0, 2, 6, 9, 5])
print(result) # True