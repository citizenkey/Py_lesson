'''Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
                          Физика:   30(л)      —      10(лаб)
                     Физкультура:     —      30(пр)      —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''

with open('file_6.txt', 'r', encoding='utf-8') as file:
    result ={}
    for x in file:
        a = x.split()
        summ = 0
        for i in a:
            z = i.split('(')
            if z[0].isnumeric():
                summ += int(z[0])
        result[a[0]] = summ
    print(result)

    # my_dict = dict()
    # with open('6.txt') as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         splitted_line = line.split()
    #         subject = splitted_line[0]
    #         sum_lessons = sum([int(x[:x.find('(')]) for x in splitted_line[1:] if '(' in x])
    #         my_dict[subject] = sum_lessons
    # print(my_dict)