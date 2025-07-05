
from GAUS import *
from rozszerzenie import *

import numpy as np
A =([
    [1, -3, 4, 6.8, 9],
    [-3,2, 4.6, 6.3, -10],
    [2, -1, 2.8, -8.4, -5],
    [-6, 2, 7, -0.5, -0.9],
    [5, -2, -0.5, 12, -4]
])

B = (74.64,-40.26,-2.32,12.6,-8.9);


n = len(A)

A_roz =rozszerzenie(A, B,n)

for i in A:
    print(i)

print("ROZSZERZONA:")
for i in A_roz:
    print(i)


print("\n\n")
Eliminacja_Gausa(A_roz,B,n)

