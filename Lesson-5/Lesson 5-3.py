'''Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину
их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
'''
with open('file_3.txt', 'r', encoding='utf-8') as file:
    # salary = 0
    # i = 0
    # for x in file:
    #     a = x.split(' ')
    #     if int(a[1]) < 20000:
    #         print(a[0])
    #     salary += int(a[1])
    #     i += 1
    # print(salary/i)

    salaries = []
    lines = file.readlines()
    for line in lines:
        name, salary = line.split(' ')
        salaries.append(int(salary))
        if int(salary) < 20000:
            print(line.strip()) # line, end=''
    print(f'\nСредняя зп:', sum(salaries) / len(salaries))