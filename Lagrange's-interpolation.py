def licznik(wezly_interpolacji, i, wartosc):
    result = 1.0
    for j in range(len(wezly_interpolacji)):
        if j != i:  # Pomijamy x-xi
            result *= (wartosc - wezly_interpolacji[j])
    return result

def mianownik(wezly_interpolacji, i):
    result = 1.0
    for j in range(len(wezly_interpolacji)):
        if j != i:  # Pomijamy xi-xi
            result *= (wezly_interpolacji[i] - wezly_interpolacji[j])
    return result

def wielomian_bazowy(wezly_interpolacji, i, wartosc):
    return licznik(wezly_interpolacji, i, wartosc) / mianownik(wezly_interpolacji, i)

def interpolacja_L4(wezly_interpolacji, wartosci_funkcji, wartosc):
    wynik = 0
    for i in range(len(wezly_interpolacji)):
        wynik += wartosci_funkcji[i] * wielomian_bazowy(wezly_interpolacji, i, wartosc)
    return wynik


wezly_interpolacji = [-2, -1, 0, 1, 2]
wartosci_funk = [5, -2, 4, -7, 2]


x = 0.5
L4_wartosc = interpolacja_L4(wezly_interpolacji, wartosci_funk, x)
print(f"L4({x}) = {L4_wartosc}")


for i in range(len(wezly_interpolacji)):
    li_wartosc = wielomian_bazowy(wezly_interpolacji, i, x)
    print(f"l{i}({x}) = {li_wartosc}")


punkty_x = [-1.5, -0.5, 0.5, 1.5]
for x in punkty_x:
    L4_wartosc = interpolacja_L4(wezly_interpolacji, wartosci_funk, x)
    print(f"L4({x}) = {L4_wartosc}")