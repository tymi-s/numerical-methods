wsp=[1,1,1,1,1]# 4 stopien wielomianu
punkty=(1,2,3,4,5)
stopien = len(wsp) -1



def Newton(wsp,punkty,stopien,wartosc):
    a0=wsp[0]
    wynik = a0
    l=len(punkty)

    while i < l:
        wynik+= wsp[i+1]*(wartosc - punkty[i])
        i+=1

