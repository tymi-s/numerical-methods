from f1 import *
from f2 import *
from transformacja import *
def GAUSS(a,b,funkcja,l_wezlow):


######################### DANE Z TABELII:

    x1=[-0.57735,0.57735]#0,1
    w1=[1,1]

    x2=[-0.774597,0,0.774597]#0,1,2
    w2=[0.555556,0.888889,0.555556]

    x3=[-0.861136,-0.339981,0.339981,0.861136] #0,1,2,3
    w3=[0.347855,0.652145,0.652145,0.347855]

    x4=[-0.906180,-0.538469,0,0.538469,0.906180]#0,1,2,3,4
    w4=[0.236927,0.478629,0.568889,0.478629,0.236927]

##########################################################



    if l_wezlow ==2:
        x = x1
        w = w1
    elif l_wezlow==3:
        x = x2
        w = w2
    elif l_wezlow==4:
        x = x3
        w = w3
    elif l_wezlow==5:
        x = x4
        w = w4
    else:
        print("Błędna liczba węzłów. Ten algorytm obsługuje tylko liczbę węzłów równą 2,3,4 lub 5")
        return

    calka =0

    for xi,wi in zip(x, w):
        calka += wi*transformacja(xi,a,b,funkcja)

    return calka





