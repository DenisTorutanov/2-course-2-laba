import numpy as np
from numpy import linalg

matrix_size = int(input('Введите размерность квадратной матрицы:'))
while (matrix_size < 4) or (matrix_size > 16):
    matrix_size = int(input("\nЧисло не находится в заданном диапазоне. \nВведите другое число:"))

x = np.random.randint(-10, 10, size=(matrix_size, matrix_size))
rang = np.linalg.matrix_rank(x)
print("Матрица:\n", x)
print("Ранг матрицы:", rang)

t = int(input('\nВведите количество знаков после запятой:'))
t = (10**(-t))

n = 1
numb_of_factorial = 1
znam_factorial = 1
temp_result = 1
sum = 0
temp_sum = 0

while abs(temp_result) > t:
    temp_sum += sum
    numb_of_fact = n
    sum += (np.linalg.det(abs(x * numb_of_factorial))) / znam_factorial
    n += 1
    znam_factorial *= (n-1) * n
    temp_result = abs(temp_sum-sum)
    temp_sum = 0
    print(n-1, ':', sum, ' ', temp_result)

print("Сумма знакопеременного ряда равна: ", sum)
