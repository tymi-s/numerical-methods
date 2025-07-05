def postac_naturalna(wspolczynniki,wartosc,stopien): #funkcja ma obliczać wartość wielomianu dla podanych parametrów
    i =0
    wynik=0
    while i < len(wspolczynniki):
        wynik += wspolczynniki[i]*wartosc**i
        i+=1
    return wynik

wsp=[1,1,1,1,1]# 4 stopien wielomianu
war=2
stopien = len(wsp) -1


wynik = postac_naturalna(wsp,war,stopien)
print("Wielomian o współczynnikach:")

for i in wsp:
    print(i, end= " ")
print("\ni stopniu rówym - " ,stopien," i dla argumentu x równego - " ,war," wartosc wynosi - ",wynik)




