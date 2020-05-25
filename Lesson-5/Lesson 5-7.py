'''Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна
содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней
прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.

'''
import json
try:
    with open('file_7.txt') as file:
        list_result = []
        result = {}
        result_2 = {}
        average = 0
        i = 0
        for line in file:
            a = line.split()
            profit = int(a[2]) - int(a[3])
            if profit > 0:
                average += profit
                i += 1
            result[a[0]] = profit
        result_2['Averege_profit'] = round(average / i)
        list_result.append(result)
        list_result.append(result_2)
        print(list_result)


    with open("file_7.json", "w") as write_f:
        json.dump(list_result, write_f)

except FileNotFoundError:
    print('Невозможно открыть фаил')