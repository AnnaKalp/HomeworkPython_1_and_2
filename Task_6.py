"""Напишите программу, которая решает
квадратные уравнения даже если
дискриминант отрицательный.
✔ Используйте комплексные числа
для извлечения квадратного корня."""

from cmath import sqrt

def solve_eq(a, b, c):
    d = b ** 2 - 4 * a * c
    z = sqrt(d)

    if d == 0:  # если дискриминант равен нулю
        x = -b / (2 * a)
        return x, x
    elif d > 0:  # если дискриминант положительный
        x1 = (-b + z) / (2 * a)
        x2 = (-b - z) / (2 * a)
        return x1, x2
    else:  # иначе дискриминант отрицательный
        x1 = (-b + z) / (2 * a)
        x2 = (-b - z) / (2 * a)
        return x1, x2


a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

x1, x2 = solve_eq(a, b, c)
print("Корни уравнения:")
print("x1 =", x1)
print("x2 =", x2)
