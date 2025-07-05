from Lib.Eulera import Euler
from Lib.Euler_zmodyfikowany  import *
from Eulera import *
from matplotlib import pyplot as plt
from Lib.Heuna_ulepszony_Euler import *
###########################################################ZADANIE 1:

alfa0 = -1e-12
beta0 = 0
kroki0 = [10,1,0.1,0.01]
czas_koncowy0 = 300
print("Zad1")
Euler(czas_koncowy0, kroki0,alfa0,beta0)

##########################################################ZADANIE 3:
print("\n\nZad3")
#alfa3= -1e-9
alfa3= -1e-12
beta3 = 0
kroki3 = [10,1,0.1,0.01]
czas_koncowy3 = 300

Euler_zmodyfikowany(czas_koncowy3, kroki3,alfa3,beta3)

##############################################################ZADANIE 2:

#alfa2= -1e-9
alfa2= -1e-12
beta2= 0
kroki2 = [10,1,0.1,0.01]
czas_koncowy2 = 300
print("\n\nZad2")
Heun(czas_koncowy2, kroki2,alfa2,beta2)























