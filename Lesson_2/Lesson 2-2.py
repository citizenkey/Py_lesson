# 2.Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
result_list = []
i = int(input("введи кол-во вводимых значений от '1' до '9':"))
while True:
    n = int(input("введи  значение:"))
    result_list.append(n)
    i -=1
    print(f'осталось {i} раз')
    if i == 0: break
print(result_list)

for i in range(1, len(result_list), 2):
    result_list[i - 1], result_list[i] = result_list[i], result_list[i - 1]
print(result_list)