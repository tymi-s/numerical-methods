import numpy as np
import matplotlib.pyplot as plt
from iloczyn_skalarny import *
from GramaSchmidta import *


def sprawdz_ortogonalnosc(funkcje_bazowe, a, b):

    n = len(funkcje_bazowe)
    iloczyny_skalarne = np.zeros((n, n))

    # wszystkie pary iloczynów skalarnych:
    for i in range(n):
        for j in range(n):
            iloczyny_skalarne[i, j] = iloczyn_skalarny(funkcje_bazowe[i], funkcje_bazowe[j], a, b)




    ortogonalna = True
    for i in range(n):
        for j in range(n):
            if i != j and abs(iloczyny_skalarne[i, j]) > 1e-10:
                ortogonalna = False

    if ortogonalna:
        print(f"Baza jest ortogonalna")
    else:
        print(f"Baza NIE jest ortogonalna")

    print()
    return iloczyny_skalarne


def rysuj_funkcje_bazowe(funkcje_bazowe, a, b, nazwa_przedzialu):
    i=0.5
    x = np.linspace(a, b, 1000)
    plt.figure(figsize=(10, 6))

    for i, funkcja in enumerate(funkcje_bazowe):
        y = np.array([funkcja(xi) for xi in x])
        plt.plot(x, y, label=f"$g_{i}(x)$")

    plt.title(f"przedział {nazwa_przedzialu}")

    plt.grid(True)
    plt.plot(f"baza_ortogonalna_.png",color = "blue")
    plt.show()
    plt.close()
    i+=0.33


def sprawdz_i_rysuj(n, przedzialy):

    for a, b in przedzialy:
        print(f"\nPrzedział [{a}, {b}]:")
        


        baza = ortogonalizacja_grama_schmidta(n, a, b)


        iloczyny = sprawdz_ortogonalnosc(baza, a, b)


        rysuj_funkcje_bazowe(baza, a, b, f"[{a}, {b}]")