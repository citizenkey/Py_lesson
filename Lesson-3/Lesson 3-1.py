# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def devide (num_1, num_2):
    try:
        c = num_1 / num_2
    except ZeroDivisionError:
        return ('Деление на ноль!')
    except ValueError:
        return ('Ошибка числа!')
    return(round(c,2))

a = input('введи число 1: ')
b = input('введи число 2: ')

print(devide(a, b))



