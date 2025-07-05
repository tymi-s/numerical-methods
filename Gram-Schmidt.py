import numpy as np
from scipy import integrate
from iloczyn_skalarny import *

def funkcja_bazy_standardowej(k):
    return lambda x: x**k


def ortogonalizacja_grama_schmidta(n, a, b):


    f = [funkcja_bazy_standardowej(k) for k in range(n)]


    g = []

    for i in range(n):

        g_i = f[i]


        for j in range(len(g)):


            g_j = g[j]
            licznik = iloczyn_skalarny(f[i], g_j, a, b)
            mianownik = iloczyn_skalarny(g_j, g_j, a, b)
            wspolczynnik = licznik / mianownik
            print(f"wspolczynnik wielomianu =", wspolczynnik)

            rzut = lambda x, coef=wspolczynnik, funkcja_bazowa=g_j: coef * funkcja_bazowa(x)


            stare_g_i = g_i
            g_i = lambda x, stare=stare_g_i, rzut=rzut: stare(x) - rzut(x)


        g.append(g_i)

    return g