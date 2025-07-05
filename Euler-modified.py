import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
def Euler_zmodyfikowany(czas_koncowy1,kroki1,alfa1,beta1):

    tabela = []
    ##############################################################LICZENIE ILOSCI ITERACJI:
    for h in kroki1:
        N = int(czas_koncowy1 / h)

        krok_czasowy =[]
        temp_w_czasie = []

        T = np.float64(1200)
        t = 0

        krok_czasowy.append(t)
        temp_w_czasie.append(T)

#######################################################EULER ZMODYFIKOWANY:
        for i in range(N):
            T_do_4 = T ** 4
            nachylenie1 = alfa1 * (T_do_4 - beta1)
            T_new = T + h * nachylenie1

            T_new_do4 = T_new ** 4
            nachylenie2= alfa1*(T_new_do4 - beta1)

            T_new = T + h * nachylenie2 # nachylenie w środku kroku
            T = T_new
            t = t + h


            #zapis danych do wykresu :D
            krok_czasowy.append(t)
            temp_w_czasie.append(T)

        ###############################################################RYSOWANIE I TABELKA:
        plt.plot(krok_czasowy, temp_w_czasie, label=f'{h}s')
        blad = abs(T - 877)
        tabela.append({
            'Krok czasowy': h,
            'Liczba iteracji': len(krok_czasowy) - 1,
            'Blad względem 877 K': blad,
            'Temperatura końcowa': T
        })
    df = pd.DataFrame(tabela)
    print(df)

    ###############################################################DO WYKRESU:

    plt.xlabel('Czas')
    plt.ylabel('Temp')
    plt.title('Euler')
    plt.legend()
    plt.grid(True)
    plt.show()


