def horner(wspolczynniki, wartosc, stopien=None):
    if stopien is None:
        stopien = len(wspolczynniki) - 1  # najw stopien wielomianu

    wynik = wspolczynniki[0]
    for i in range(1, stopien + 1):
        wynik = wynik * wartosc + wspolczynniki[i]

    return wynik


wspolczynniki = [0.5, 1.333, -13.0 / 6, -2]

print(horner(wspolczynniki, 2))
print(horner(wspolczynniki,0))
print(horner(wspolczynniki,-4))