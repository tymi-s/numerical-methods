def Newtona(funkcja, pochodna1, start_point, epsilon=1e-6, max_iter=100):
    x = start_point
    for i in range(max_iter):
        f = funkcja(x)
        df = pochodna1(x)

        if df == 0:
            return None

        x_new = x - f / df

        if abs(x_new - x) < epsilon:
            return x_new

        x = x_new


    return x