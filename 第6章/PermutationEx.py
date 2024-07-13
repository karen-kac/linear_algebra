import sympy.combinatorics as symc

S = symc.Permutation([5, 3, 6, 4, 7, 0, 1, 8, 2])
print('S = ', S)
print('inverse of S = ', S**-1)
print('order of S = ', S.order())
print(S.transpositions()[::-1])