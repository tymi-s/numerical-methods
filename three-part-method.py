from iloczyn_skalarny import *
def metoda_trojczlonowa(n,a=-1,b=1):

    wielomiany = []
    P0 = lambda x: 1.0
    wielomiany.append(P0)
    if n > 1:
        P1 = lambda x: x
        wielomiany.append(P1)


    for k in range(2, n):
        # pobranie poprzedniego wielomianu
        P_prev_prev = wielomiany[k - 2]
        P_prev = wielomiany[k - 1]

        def make_polynomial(k, P_prev, P_prev_prev):
            def P_k(x):
                return ((2 * k - 1) * x * P_prev(x) - (k - 1) * P_prev_prev(x)) / k

            return P_k

        P_k = make_polynomial(k, P_prev, P_prev_prev)
        wielomiany.append(P_k)

    return wielomiany


def normalizuj_wielomiany(wielomiany_legendre):

    wielomiany_znormalizowane = []

    for i, P in enumerate(wielomiany_legendre):
        norma = norma_funkcji(P)
        P_norm = lambda x, P_orig=P, n=norma: P_orig(x) / n
        wielomiany_znormalizowane.append(P_norm)


    return wielomiany_znormalizowane






