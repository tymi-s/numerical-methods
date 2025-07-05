import numpy as np
import scipy as sp
from funkcje import *
def zad1(f,baza_standardowa):

    A=np.zeros((5,5))


    #macierz A
    for i in range(0,5):
        for j in range(0,5):
            wynik = sp.integrate.quad(lambda x: baza_standardowa[i](x) * baza_standardowa[j](x), -1, 1)
            A[i,j] = wynik[0]

    print(f"macierz A:\n{A}")

    #wektor b:
    b = np.zeros(5)

    for i in range(5):
        wynikk = sp.integrate.quad(lambda x: f(x) * baza_standardowa[i](x), -1, 1)
        b[i] = wynikk[0]

    print(f"\n\nwektor b: {b}")

    #rozwiazanie układu równań liniowych:

    wspolczynniki_wielomianu = np.linalg.solve(A,b)
    print(f"\n\nwspoolczynniki wielomianu: {wspolczynniki_wielomianu}")
    return wspolczynniki_wielomianu




