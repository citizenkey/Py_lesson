'''Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
with open('file_5.txt', 'w+') as file:
    summ = 0
    line = input('Введите числа через пробел: ')
    file.writelines(line)
    lines = file.readlines()
    a = line.split()
    print(a)
    for i in a:
        summ += int(i)
    print(summ)
