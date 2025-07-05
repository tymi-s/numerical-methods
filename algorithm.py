from numpy import *
from printing import *
def algorytm(A,L,U,n):

    for j in range(n):
        for i in range(j+1,n):

            l=U[i][j]/U[j,j]
            L[i][j]=l
            U[i, j:] = U[i, j:] - l * U[j, j:]
    print("\nA:")
    printing(A)
    print("\nL:")
    printing(L)
    print("\nU:")
    printing(U)


