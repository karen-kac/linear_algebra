import sympy.combinatorics as symc

I = symc.Permutation(size=10)
P = symc.Permutation([2, 5, 7, 3, 6, 0, 1, 4, 8])
Q = symc.Permutation(1, 2, 3)(5, 4, 6, 9)
R = symc.Permutation(3, 4)(0, 2, 7)
print('I = ', I)
print('P =', P , 'Q =', Q , 'R =', R, sep = ' ')
print('inverse of Q = ', Q**-1)
print('QR = ', Q*R)
print('IQ = ', I*Q)
print('order of Q = ', Q.order())
print(Q.transpositions()[::-1], ': Q expressed as a product of transpositions')
print('signature of Q = ', Q.signature())