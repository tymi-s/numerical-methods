import numpy as np
import matplotlib.pyplot as plt


def lagrange_interpolation(x_points, y_points, x):
    def L(k, x):
        term = 1
        for j in range(len(x_points)):
            if j != k:
                term *= (x - x_points[j]) / (x_points[k] - x_points[j])
        return term

    return sum(y_points[k] * L(k, x) for k in range(len(x_points)))


# Przykładowe punkty interpolacji (można zmienić)
x_points = np.array([-2, -1, 0, 1, 2])
y_points = np.array([5, -2, 4, -7, 2])  # y = x^2

# Generowanie wartości w przedziale [-2, 2] co 0.01
x_values = np.arange(-2, 2.01, 0.01)
y_values = [lagrange_interpolation(x_points, y_points, x) for x in x_values]

# Wypisanie wyników
for x, y in zip(x_values, y_values):
    print(f"x = {x:.2f}, y = {y:.4f}")

# Wykres interpolacji
plt.plot(x_values, y_values, label='Interpolacja Lagrange’a', color='blue')
plt.scatter(x_points, y_points, color='red', label='Punkty danych')
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Interpolacja Lagrange’a")
plt.grid()
plt.show()
