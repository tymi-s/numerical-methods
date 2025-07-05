def horner(wspolczynniki, wartosc):
    wynik = wspolczynniki[0]
    for wsp in wspolczynniki[1:]:
        wynik = wynik * wartosc + wsp
    return wynik


wspolczynniki = [0.5, 1.333, -13.0/6, -2]


print(horner(wspolczynniki,2))
print(horner(wspolczynniki,-4))
print(horner(wspolczynniki,0))


