'''Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
with open('file_5.txt', 'w', encoding='utf-8') as file:
    # summ = 0
    # line = input('Введите числа через пробел: ')
    # file.writelines(line)
    # lines = file.readlines()
    # a = line.split()
    # print(a)
    # for i in a:
    #     summ += int(i)
    # print(summ)

    nums = input('Введите целые числа через пробел:')
    file.write(f'Введенные числа: {nums}\n')
    nums = map(int, nums.split())
    sum_numps = sum(nums)
    print(f'Сумма чисел:  {str(sum_numps)}')
    print("Все записано в файл")