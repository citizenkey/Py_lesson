# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

sec_num = int(input('введите число секунд:'))
h = sec_num //3600
m = (sec_num - h * 3600) // 60
s = (sec_num - h * 3600) % 60
print(f'{h}:{m}:{s}')



