'''
1.
Создать класс TrafficLight (светофор).
---OK---
определить у него один приватный атрибут color (цвет) и метод get_current_signal() (получить текущий цвет);
после создания экземпляра светофора, он запускает режим смены сигналов с разной длительностью: красный (3 сек),
 жёлтый (1 сек), зелёный (3 сек);
переключение идет циклично в порядке красный-жетлый-зеленый-красный-жетлый-зеленый-красный-...
проверить переключение режимов работы светофора, опрашивая в цикле текущее состояние светофора
с интервалом 0.5 секунды, используя метод get_current_signal().
!!!!!!!!!!!! Пока только так заставила его работать, опять же не хватило времени и опыта додумать как в какой-то
определенный момент выхватить результат.
'''

from time import sleep
import datetime

class TrafficLight:
    _color = ('red', 'yellow', 'green')

    def __init__(self):
        self.red = 'red'
        self.yellow = 'yellow'
        self.green = 'green'

    def get_current_signal(self):
        while True:
            print(self.red)
            sleep(3)
            print(self.yellow)
            sleep(1)
            print(self.green)
            sleep(3)

signal = TrafficLight()
# print(signal._color)
print(signal.get_current_signal())


# while True:
#     print(signal.get_current_signal())
#     sleep(0.5)





