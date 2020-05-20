# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def notes(var_1, var_2, var_3, var_4, var_5, var_6):
    print(f'Имя - {var_1}; фамилия - {var_2}; год рождения - {var_3}; '
          f'город проживания - {var_4}; email - {var_5}; телефон - {var_6}')

notes(var_1='Ivan', var_2='Ivanov', var_3=1978, var_4='Luisiana',
      var_5='qwe@rambler.ru', var_6='+198000000')

# def personal_info(**kwargs):
#     return kwargs
#
#
# print(personal_info(
#     name=input('Имя: '),
#     surname=input('Фамилия: '),
#     bitrhday=input('ДР: '),
#     city=input('Город: '),
#     email=input('Почта: '),
#     phone=input('Телефон: '),
# ))