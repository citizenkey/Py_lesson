# Спортсмен в первый день пробежал a километров. Каждый день спортсмен увеличивал результат
# на 10 % относительно предыдущего. Определить номер дня, на который результат спортсмена
# составит не менее b километров. Программа должна принимать значения параметров a и b
# и  выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3. Результат: 1-й день: 2,  2-й день: 2,2. ... 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

a = int(input('результат первого дня, в км:'))
b = int(input('жеаемый результат в день, в км:'))
i = 1
while a < b:
    temp = i
    a = a + (a / 100 * 10)
    print(f'{i}-й день {a:.2f} км ')
    i +=1
print(f'на {temp} день спорцмен пройдет не менее {int(a)} км')