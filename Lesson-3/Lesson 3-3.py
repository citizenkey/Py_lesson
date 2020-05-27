# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(var_1, var_2, var_3):
    c = [var_1, var_2, var_3]
    print(sorted(c, reverse=True))
    summ = c[0] + c[1]
    return summ


a = my_func(var_1=40, var_2=20, var_3=2)
print(a)

