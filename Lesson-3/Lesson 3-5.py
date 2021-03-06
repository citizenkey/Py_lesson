'''5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к
уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы
завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
сумму этих чисел к полученной ранее сумме и после этого завершить программу.
'''

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


summ = 0
exit_all = False
while True:
    x = input('Выход - Q, \nВведите числа через пробел: ')
    numbers = x.split()
    i = 0
    for i in numbers:
        if is_integer(i):
            summ += int(i)
        else:
            print('сумма введенных чисел', summ)
            exit_all = True
            break
    if x.upper() == 'Q' or exit_all == True:
        break
    print('сумма введенных чисел', summ)

# def summary():
#     exit = False
#     result = 0
#     while exit == False:
#         numbers = input('Enter numbers or q to exit: ').split()
#         res_line = 0
#         for num in numbers:
#             if 'q' in num:
#                 exit = True
#                 break
#             res_line += int(num)
#         result += res_line
#     print(result)