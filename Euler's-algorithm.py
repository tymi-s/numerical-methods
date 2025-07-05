import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def Euler(czas_koncowy, kroki, alfa, beta):
    tabela = []
##############################################################LICZENIE ILOSCI ITERACJI:
    for h in kroki:
        N = int(czas_koncowy / h)
        krok_czasowy = []
        temp_w_czasie = []
        T = np.float64(1200)
        t = 0

        #zapis danych do wykresu :D
        krok_czasowy.append(t)
        temp_w_czasie.append(T)

        ###################################################################EULER:
        for i in range(N):

                T_do_4 = T ** 4
                nachylenie = alfa * (T_do_4 - beta)


                T_new = T + h * nachylenie
                T = T_new
                t = t + h

                # Zapisz wyniki
                krok_czasowy.append(t)
                temp_w_czasie.append(T)
        ###############################################################RYSOWANIE I TABELKA:

        plt.plot(krok_czasowy, temp_w_czasie,label=f'{h}s')
        blad = abs(T - 877)
        tabela.append({'Krok czasowy': h,'Liczba iteracji': len(krok_czasowy) - 1,'Blad względem 877 K ':blad ,'Temperatura końcowa': T})
    df = pd.DataFrame(tabela)
    print(df)

    ###############################################################DO WYKRESU:

    plt.xlabel('Czas')
    plt.ylabel('Temp')
    plt.title('Euler - zmodyfikowany')
    plt.legend()
    plt.grid(True)
    plt.show()