'''Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''
i = 0
with open('file_4.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for x in lines:
        a = x.split(' ')
        if a[i] == 'One':
            a[i] = 'Один'
        elif a[i] == 'Two':
            a[i] = 'Два'
        elif a[i] == 'Three':
            a[i] = 'Три'
        else:
            a[i] = 'Четыре'
        with open('file_4_write.txt', 'a', encoding='utf-8') as file:
            file.writelines(a)
        print(a)
