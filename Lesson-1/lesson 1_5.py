# Запросить значения выручки и издержек. Определите, с каким финансовым результатом работает
# фирма (прибыль  или убыток ). Если фирма отработала с прибылью, вычислить рентабельность выручки
# (соотношение прибыли к выручке). запросите численность сотрудников фирмы и определите прибыль фирмы
# в расчете на одного сотрудника.

revenue = float(input('введите сумму выручки_'))
cost = float(input('введите сумму издержек_'))
result = revenue - cost
profit = result / revenue
if revenue > cost:
    print(f'Прибыль за период составляет: {result:.2f}')
    print(f'Рентабильность выручки: {profit:.2%}')
    stuff_num = int(input('\nВведите численность сотрудников '))
    profit_byperson = result / stuff_num
    print('прибыль на одного сотрудника составляет: {:,.2f}'.format(profit_byperson))
else:
    print("\nУбыток за период составляет:", -result)