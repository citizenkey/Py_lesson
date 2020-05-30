'''Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала!')

    def stop(self):
        print(f'{self.name} остановилась!')

    def turn(self, direction):
        print(f'{self.name} повернула на {direction}!')

    def show_speed(self):
        print('Скорость:', self.speed)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Привышение скорости!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print('Скорость:', self.speed)
        if self.speed > 40:
            return ('Привышение скорости!')


class PoliceCar(Car):
    pass


sport_car = SportCar(240, 'Красная', 'крутая спортивная тачка', False)
town_car = TownCar(140, 'Черная', 'городской седан', False)
work_car = WorkCar(90, 'Белая', 'мини-бус', False)
police_car = PoliceCar(210, 'Полосаятая', 'полицейская', True)

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.turn('право')