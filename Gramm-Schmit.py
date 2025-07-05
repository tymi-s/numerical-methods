from iloczyn_skalarny import *


def grammaShmita(baza_standardowa):
    baza_ortogonalna = []


    v1 = baza_standardowa[0]
    norma1 = norma_funkcji(v1)
    u1 = lambda x: v1(x) / norma1
    baza_ortogonalna.append(u1)  #pierwszy element bazy ortogonalnej



    for i in range(1, len(baza_standardowa)):
        vi = baza_standardowa[i]
        ui = vi

        for j in range(i):
            uj = baza_ortogonalna[j]
            projekcja_skalar = iloczyn_skalarny(vi, uj)
            ui_poprzednie = ui
            ui = lambda x, ui_prev=ui_poprzednie, coeff=projekcja_skalar, u_j=uj: ui_prev(x) - coeff * u_j(x)

        norma_ui = norma_funkcji(ui)
        ui_znormalizowane = lambda x, u=ui, n=norma_ui: u(x) / n

        baza_ortogonalna.append(ui_znormalizowane)



    return baza_ortogonalna