# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью
# оператора **. Второй — более сложная реализация без оператора **, предусматривающая
# использование цикла.
x = float(input('Введи число x>0: '))
y = int(input('Введи число y<0: '))
def my_func_1(x, y):
    temp = 1
    for i in range(abs(y)):
        temp = x * temp
    result = 1 / temp
    return result

a = my_func_1(x, y)
print('первый вариант: ', a)


def my_func_2(x, y):
    return x ** y

b = my_func_2(x, y)
print('второй вариант: ', b)

