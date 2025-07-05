from GAUSS import *
from f1 import *
from f2 import *
def transformacja(t,a,b,funkcja):
    x= (b-a)*0.5*t +(a+b)*0.5
    return funkcja(x)*0.5*(b-a)