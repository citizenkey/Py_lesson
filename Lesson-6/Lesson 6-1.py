'''Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
'''


from time import sleep
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.__color = (('Красный', 5), ('Желтый', 2), ('Зеленый', 5))

    def running(self):
        for color, sec in cycle(self.__color):
            print(color, '(Ожидание {} sec)'.format(sec))
            sleep(sec)

traffic_light = TrafficLight()
traffic_light.running()