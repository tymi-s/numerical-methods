
def Eliminacja_Gausa(A_roz, B, n):



    for i in range(1, n):

        wiodacy = A_roz[0]
        if wiodacy[0] == 0:
            continue


        mn = A_roz[i][0] / wiodacy[0]


        for j in range(len(A_roz[i])):
            A_roz[i][j] -= wiodacy[j] * mn


    for i in A_roz:
        print(i)
    return A_roz