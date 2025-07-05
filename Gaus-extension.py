def rozszerzenie(A,B,n):
    A_rozszerzona = [row.copy() for row in A]# kopia

    for i in range(n):
        A_rozszerzona[i].append(B[i])

    return A_rozszerzona