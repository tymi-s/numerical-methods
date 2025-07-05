import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def Heun(czas_koncowy, kroki, alfa, beta):
    tabela = []
    ##############################################################LICZENIE ILOSCI ITERACJI:
    for h in kroki:

        N = int(czas_koncowy / h)


        krok_czasowy = []
        temp_w_czasie = []


        T = np.float64(1200)
        t = 0

        #punkt poczatkowy
        krok_czasowy.append(t)
        temp_w_czasie.append(T)

        ############################################################METODA HEUNA:
        for i in range(N):

            T_do_4 = T ** 4
            k1 = alfa * (T_do_4 - beta)# nachylenie w punkcie poczatkowym


            T_pred = T + h * k1


            T_pred_do_4 = T_pred ** 4
            k2 = alfa * (T_pred_do_4 - beta) #  naychlenie w punkcie końcowym


            T_new = T + h * (k1 + k2) / 2# wzor heuna

            T = T_new
            t = t + h


            krok_czasowy.append(t)
            temp_w_czasie.append(T)

        ########################################################################WYKRES I TABELA:
        plt.plot(krok_czasowy, temp_w_czasie, label=f'{h}s')
        blad = abs(T - 877)
        tabela.append({
            'Krok czasowy': h,
            'Liczba iteracji': len(krok_czasowy) - 1,
            'Blad względem 877 K': blad,
            'Temperatura końcowa': T
        })

    df = pd.DataFrame(tabela)
    print("Metoda Heuna:")
    print(df)
    #####################################################################WYGLAD WYKRESU
    plt.xlabel('Czas')
    plt.ylabel('Temp')
    plt.title('Heun')
    plt.legend()
    plt.grid(True)
    plt.show()

    return df