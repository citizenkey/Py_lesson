'''Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''
with open('file_2.txt', 'r') as file:
    lines = file.readlines()
    i = 0
    for line in lines:
        (line.strip())
        i += 1
    print(f'количество строк {i}')
    for num, j in enumerate(lines, 1):
        len_string = j.count(' ') + 1
        print(f'в {num} строке {len_string} слов(а)')

