import math


def square(x):
    return math.ceil(x*x)


x = float(input("Введите число: "))

print(f'Площадь квадрата {math.ceil(x*x)}')
