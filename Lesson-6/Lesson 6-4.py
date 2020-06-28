'''Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''
<
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):

        print('{} едет!'.format(self.name))

    def stop(self):
        print('{} останавливается!'.format(self.name))

    def turn(self, direction):
        print('{} поворачивает на {}!'.format(self.name, direction))


    def show_speed(self):
        print('Скорость:', self.speed)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:

            print('Превышаете скоростной режим!')



class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print('Скорость:', self.speed)
        if self.speed > 40:

            print ('Превышаете скоростной режим!')

class PoliceCar(Car):
    pass

sport_car = SportCar(240, 'краная', 'крутая тачка', False)
town_car = TownCar(140, 'серая', 'городская машина', False)
work_car = WorkCar(90, 'белая', 'рабочая машина', False)
police_car = PoliceCar(210, 'полосатая', 'полиуйская машина', True)

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed() # не работает уведомление о скорости
police_car.show_speed()
sport_car.turn('left')
