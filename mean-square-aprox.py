
def aproksymacjaSredniokwadratowa(stopienWiel):


    macierz = []
    wiersz = []
    for i in range(1,stopienWiel):
        for j in range(1, stopienWiel):

            mianownik = i+j
            wiersz.append(1/mianownik)

        macierz[i]=wiersz

    print(macierz)