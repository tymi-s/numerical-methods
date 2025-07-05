import numpy as np


def z_newtona_do_naturalnej(wspolczynniki, iksy):

    n=len(wspolczynniki)

    if len(iksy) != n-1:
        print("Dlugosci tablicy z wezlami powinna byc o jeden krotsza niz dlugosc tablicy z wspolczynnikami!")
        return

    result =np.zeros(n) # tablica w ktorej bedzie wynik, wypelniam ją zerami
    result[0]=wspolczynniki[0]

    for i in range(1,n):
        term = np.array([wspolczynniki[i]])

        for j in range(i):
            term = np.append(0, term)

            temp = np.zeros(len(term))
            temp[:-1] = term[1:] * (-iksy[j])
            term = term + temp

            result[:len(term)] += term

    return result


if __name__ == "__main__":

    wspolczynniki = [1, 2, 3]
    wezly = [1, 2]

    result = z_newtona_do_naturalnej(wspolczynniki, wezly)
    print("Współczynniki w postaci naturalnej:", result)